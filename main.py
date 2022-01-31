#Import FASTAPI framework
from fastapi import FastAPI

#Initialize and customize Swagger documentation
app = FastAPI(
    title="Search Algorithim API's",
    version="1.0",
    description="Search Algorithim Application"
)


# Get Item Index Function

## Api receives an Integer Item from user ----> The SearchIndex function searches for the Item 
## in a defined array and returns results.
@app.get("/item/{item}",tags=["Get Index of Item API"])
def SearchIndex(item: int):
    # Defined array
    fixed_arr = [6, 8, 4, 90, 100, 28, 12, 56, 12, 112]

    try:
        # Using the Index inbuilt function, I search for the item received in the defined array.
        result = fixed_arr.index(item)
    except:
        # Handling exception if the item received is not in the defined array.
        result = "Item not in array"
    
    # Return the result found
    return {"Item is on index": result}
