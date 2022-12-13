
# WARNING: Don't change it in production, otherwise clients will lose their existing payments.
# There's not much need to hide it in .env, so, just define it there.
BILL_ID_SALT = '0rb?:RuRIxB5OV@eep5kM'

MONEY_PER_MINUTE = 1

# Withdrawal rubles commission, default it's 10%
WITHDRAWAL_COMMISSION = 0.1
