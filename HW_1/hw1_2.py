import abc
import json
import pickle

BASE_FILE_NAME = 'data'


class SerializationInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def serialize(self, data):
        pass

    @abc.abstractmethod
    def deserialize(self, data):
        pass


class JsonSerialization(SerializationInterface):
    def serialize(self, data):
        with open(BASE_FILE_NAME + '.json', 'w') as f:
            json.dump(data, f)

    def deserialize(self, data):
        with open(BASE_FILE_NAME + '.json', 'r') as f:
            return json.load(f)


class BinSerialization(SerializationInterface):

    def serialize(self, data):
        with open(BASE_FILE_NAME + '.bin', 'wb') as f:
            pickle.dump(data, f)

    def deserialize(self, data):
        with open(BASE_FILE_NAME + '.bin', 'rb') as f:
            return pickle.load(f)


if __name__ == "__main__":
    data = {'name': "Sasha", 'age': 22, 'city': "Odessa"}
    data_json = JsonSerialization()
    data_bin = BinSerialization()
    data_json.serialize(data)
    data_bin.serialize(data)

    print(data_json.deserialize(data))
    print(data_bin.deserialize(data))
    print(data)




