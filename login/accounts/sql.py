from django.db import connection

def my_custom_sql(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT image FROM public.hash_location WHERE hashimage = %s", [self.hashimage])
        row = cursor.fetchone()
        print(row)
    return row
def getlonlat(hi):
    with connection.cursor() as cursor:
        cursor.execute("SELECT latitude,longitude FROM public.hash_location WHERE hash = %s", [hi])
        row = cursor.fetchone()
        print(row)
    return row
def get_img(hash):
    with connection.cursor() as cursor:
        cursor.execute("SELECT image FROM public.hash_location WHERE hashimage = %s", [hash])
        row = cursor.fetchone()
        print(row)
    return row