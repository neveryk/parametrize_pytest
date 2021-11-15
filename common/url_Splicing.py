class reque_ping():
    def url_jia(self,data):
        l=[]
        for a,b in data.items():
            l.append(a + '=' + str(b))
        data_string="&".join(l)
        get_url="?"+data_string
        return get_url
ur=reque_ping()

