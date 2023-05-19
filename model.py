import pickle
import datetime
import warnings
warnings.filterwarnings('ignore')
predictor = pickle.load(open('Model.pkl','rb'))
loction = pickle.load(open('location.pkl','rb'))
def mal_function_pred(dc,dp,dt,place,day,mon,year):
    loc = loction.transform([[place]])[0]
    days=predictor.predict([[dc,dp,dt,loc]])[0]
    mal_fun = datetime.datetime(year,mon,day)+ datetime.timedelta(days=days)
    ser_req = datetime.datetime(year,mon,day)+ datetime.timedelta(days=days-30)
    return mal_fun,ser_req