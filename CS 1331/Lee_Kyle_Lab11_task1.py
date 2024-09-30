def trigger_exceptions():
    try:
        num = 10
        num += '5'
        
        int('abc')
        
        my_dict = {'key': 'value'}
        print(my_dict['invalid_key'])
        
        my_list = [1, 2, 3]
        my_list.split()
        
        def infinite_recursion():
            return infinite_recursion()
        
        infinite_recursion()
    
    except TypeError as e:
        print("TypeError occurred:", e)
    except ValueError as e:
        print("ValueError occurred:", e)
    except KeyError as e:
        print("KeyError occurred:", e)
    except AttributeError as e:
        print("AttributeError occurred:", e)
    except RecursionError as e:
        print("RecursionError occurred:", e)

if __name__ == "__main__":
    trigger_exceptions()
