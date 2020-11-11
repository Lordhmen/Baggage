def create_date_base(n):
    data_base = open(n, "r", encoding="utf-8")
    db = []
    for line in data_base.readlines():
        db += [line.split()]
    return db
# for i in db:
#     i[3] = int(i[3])
#     i[4] = int(i[4])
