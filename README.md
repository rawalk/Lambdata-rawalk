# Lambdata-rawalk
Collection of information for creating packages and lesson information. 

## contents: 
contains three functions. 
enlarge, test_train_val_split, and a name class. 

## testpypi location and Installation: 
```py
pip install -i https://test.pypi.org/simple/ lamdata-dspt6-rawalk==1.0.1
```

## Usage

```py
# In a new cell type out the following: 
from my_lambdata.ds_utilities import enlarge

# in a new cell type out the following: 
x = 11
print(enlarge(x))
```

```py
# In a new cell import the following class: 
from my_lambdata.ds_utilities import train_validation_test_split

# in a new cell type out the follwoing: 
X_train, X_val, X_test, y_train, y_val, y_test = train_validation_test_split(X, y)