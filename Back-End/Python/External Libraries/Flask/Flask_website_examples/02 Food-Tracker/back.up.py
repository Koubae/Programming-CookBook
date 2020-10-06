  if request.args.get('search'):
        # print(request.args.get('search'))
        month = request.args.get('search')
        cur = db.execute(query_all_month, ['July'])
        print([request.args.get('search')])
        results = cur.fetchall()
        print(results)
        date_results = show_days(results)
        all_month = get_month(date_results)
        
        print(date_results)
        return render_template('index.html', results=date_results, all_month=all_month)
    
    elif not request.args.get('search'):
     

    
        # Query all days and show DESC/ASC
        cur = db.execute(query_all_days)
        results = cur.fetchall()
        # Get proccesed values from query_data.py 
        date_results = show_days(results)
        for i in date_results:
           
            print(i['pretty_date'])
        all_month = get_month(date_results)
    
        return render_template('index.html', results=date_results, all_month=all_month)  