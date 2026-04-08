import json

start_id = 111

def create_data():
    global start_id

    data = {
        "id": start_id,
        "temperature": 25.0,
        "humidity": 60,
        "status": "OK"
    }

    start_id += 1
    return data


def print_data(data: dict):
    print("----- DATA RECEIVED -----")
    print(f"ID: {data.get('id')}")
    print(f"Temperature: {data.get('temperature')} °C")
    print(f"Humidity: {data.get('humidity')} %")
    print(f"Status: {data.get('status')}")
    print("-------------------------")