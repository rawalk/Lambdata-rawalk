import pandas as pd
from sklearn.model_selection import train_test_split
def enlarge(n):
    ''' This function will multiple input by 100 '''
    return n * 100

def test_train_val_split(X):
    ''' This function will do test, train and validation split '''
  X_train, X_test, y_train, y_test = train_test_split(X, test_size=0.2, random_state=1)
  X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=1) # 0.25 x 0.8 = 0.2
  return X_train, X_val, X_test, y_train, y_val, y_test

def len_counter(n):
    n = "294T Cells"
    return len(n)

if __name__ == '__main__':
    y = int(input("choose a number: "))
    print(y, enlarge(y))