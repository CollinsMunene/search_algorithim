# Search Algorithm

Search Algorithm is a simple Python-based algorithm developed using Fast-Api with the aim of returning the index of an item in an array in a simple manner.

## How it works ...

The algorithm contains a single API that receives an Integer Item from the user and the algorithm then searches the defined array for the index position of the item passed.

Defined variables:-
   The Array -> [6, 8, 4, 90, 100, 28, 12, 56, 12, 112];

Inbuilt Function used:- Index


 
Example:
```python

#I as the user would like to get the index position of item 4
#So my API would look something like below
http://127.0.0.1:8000/item/4



#Using the defined array below
    fixed_arr = [6, 8, 4, 90, 100, 28, 12, 56, 12, 112]

    try:
        # Using the Index inbuilt function, I search for the item received in the defined array.
        result = fixed_arr.index(4)
    except:
        # Handling exception if the item received is not in the defined array.
        result = "Item not in array"
    
    # Return the result found
    return {"Item is on index": result}


#The algorithm will return the result as the Index position 2

```

## Firing it up ...

To fire up the algorithm, follow the following steps.

## Install
You will need to create a virtual environment using the virtualenv library as below.
```sh
git clone https://github.com/CollinsMunene/search_algorithim.git

cd search_algorithim 

virtualenv venv

source venv/bin/activate

pip install -r requirements.txt
```

## Usage

```sh
uvicorn main:app --reload
```

Once the application is running, the available api is 
```sh
http://127.0.0.1:8000/item/{pass in any item}
```

## Author

👤 **Collins H. Munene**

* Website: [My portfolio](https://collinsmunene.github.io/collinshillary.github.io/)
* Twitter: [@Hillary Collins](https://twitter.com/HillaryCollns)
* Github: [@Collins Munene](https://github.com/CollinsMunene)
* LinkedIn: [@Collins Munene](https://linkedin.com/in/collins-hillary-munene)