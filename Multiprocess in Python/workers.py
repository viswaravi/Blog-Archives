def process_rows(data):
    d = data[0]
    df = data[1]
    for index,row in df.iterrows():
        e_c = int(row['pt_ecode1'])
        month = int(row['pt_date'].month)
        prod_eff = int(row['prod_eff'])
        if (e_c,month) in list(d.keys()):
            d[e_c,month] = (prod_eff+d[e_c,month])/2
        else:
            d[e_c,month] = prod_eff