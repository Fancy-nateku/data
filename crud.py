from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import Expense
from schemas import ExpenseCreate, ExpenseUpdate

async def get_expense(db: AsyncSession, expense_id: int):
    result = await db.execute(select(Expense).where(Expense.id == expense_id))
    return result.scalars().first()

async def get_expenses(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Expense).offset(skip).limit(limit))
    return result.scalars().all()

async def create_expense(db: AsyncSession, expense: ExpenseCreate):
    db_expense = Expense(**expense.dict())
    db.add(db_expense)
    await db.commit()
    await db.refresh(db_expense)
    return db_expense

async def update_expense(db: AsyncSession, expense_id: int, expense: ExpenseUpdate):
    db_expense = await get_expense(db, expense_id)
    if not db_expense:
        return None
    for key, value in expense.dict(exclude_unset=True).items():
        setattr(db_expense, key, value)
    db.add(db_expense)
    await db.commit()
    await db.refresh(db_expense)
    return db_expense
async def delete_expense(db: AsyncSession, expense_id: int):
    db_expense = await get_expense(db, expense_id)
    if not db_expense:
        return None
    await db.delete(db_expense)
    await db.commit()
    return db_expense