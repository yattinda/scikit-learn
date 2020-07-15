import pandas as pd

data = {"Name":["mukai","tabuchi","nakao","inazawa"],
        "Location":["Hakata","Hakata","Hakata","Hakata"],
        "Constitute":["Vo&gi","gi","ba","br"]
        }

data_pandas = pd.DataFrame(data)

#Ipython.displayでDataFlameをJupyter notebookで表示
display(data_pandas)

display(data_pandas["gi" == data_pandas.Constitute])

#inは使えなかった
