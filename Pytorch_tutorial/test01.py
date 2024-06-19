import torch
import numpy as np
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torch.utils.data as Data


def fizzbuzz_encode(number):
    '''
    number: int
    '''

    if number % 15 == 0:
        return 3 #'fizzbuzz'
    elif number % 5 == 0:
        return 2 #'buzz'
    elif number % 3 == 0:
        return 1 #'fizz'
    return 0 #str(number)

def fizzbuzz_decode(number, label):
    '''
    number: int
    label: 0 1 2 3
    '''

    return [str(number), 'fizz','buzz','fizzbuzz'][label]

def helper(number):
    print(fizzbuzz_decode(number, fizzbuzz_encode(number)))

for number in range(1,16):
    helper(number)

#To provide more info 
NUM_DIGIRS = 10
def binary_encode(number):
    return np.array([number >> d & 1 for d in range(NUM_DIGIRS)][::-1])

x_train= torch.Tensor([binary_encode(number) for number in range(101, 1024)])
y_train = torch.Tensor([fizzbuzz_encode(number) for number in range(101, 1024)])


class MyDataset(Data.Dataset):
    def __init__(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

    def __getitem__(self, idx): #101 79 x xxxx xx ...
        return self.x_train[idx], self.y_train[idx]
    
    def __len__(self):
        return len(self.y_train)

train_dataset = MyDataset(x_train, y_train)
train_loader = Data.DataLoader(train_dataset, batch_size=16, shuffle=True)

iter(train_loader)




