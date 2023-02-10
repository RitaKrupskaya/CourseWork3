from utils import get_data, get_filtered, get_reformatted, get_last_operations

def main():
    BANK_OPERATIONS_URL = "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230210T151236Z&X-Amz-Expires=86400&X-Amz-Signature=49e7e60535fb6e7835c06f25301c449b2f38ff40ae69f040dd40837d60ce29ef&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22operations.json%22&x-id=GetObject"
    FROM_NONE = True
    LAST_OPERATIONS = 5

    data = get_data(BANK_OPERATIONS_URL)

    data = get_filtered(data, from_none=FROM_NONE)
    data = get_last_operations(data, LAST_OPERATIONS)
    data = get_reformatted(data)

    for i in data:
        print(i, end='\n\n')


if __name__ == '__main__':
    main()
