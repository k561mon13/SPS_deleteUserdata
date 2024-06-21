import pyodbc
import json

config = json.loads(open("config.json").read())

"""
userids skal indeholde en iterable (list, tuple, set el.lign.) med de brugernavne, der skal have slettet deres data.
"""
userids = tuple(userid[:-1] for userid in set(open("Inaktive i datacatalog.csv").readlines()+open("Inaktive i themecatalog.csv").readlines()))

conn = pyodbc.connect(**config.get("credentials"))
crsr = conn.cursor()

userdata_get_tables_sql = f"select tablename from [userdatasystem].[datacatalog] where userid in {userids} {('and permissions=0' if config.get('deletePublic', False)  is False else '')}"
userdata = tuple(row[0] for row in crsr.execute(userdata_get_tables_sql))
for ud in userdata:
    sql = f"DROP TABLE userdata.{ud}"
    print(sql)
    crsr.execute(sql)

userdata_delete_index_sql = f"delete from [userdatasystem].[datacatalog] where userid in {userids} {('and permissions=0' if config.get('deletePublic', False)  is False else '')}"
print(userdata_delete_index_sql)
crsr.execute(userdata_delete_index_sql)

themecatalog_delete_index_sql = f"delete from [userdatasystem].[themecatalog] where userid in {userids} {('and permissions=0' if config.get('deletePublic', False)  is False else '')}"
print(f"delete from [userdatasystem].[themecatalog] where userid in {userids} {('and permissions=0' if config.get('deletePublic', False)  is False else '')}")
crsr.execute(themecatalog_delete_index_sql)