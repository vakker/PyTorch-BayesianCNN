import numpy as np
import torch
import torchvision
import torchvision.transforms as transforms
from torch.utils.data.sampler import SubsetRandomSampler

def getDataset(dataset):
    transform = transforms.Compose([
        transforms.Resize((32, 32)),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(10),
        transforms.ToTensor(),
        ])

    if(dataset == 'CIFAR10'):
        trainset = torchvision.datasets.CIFAR10(root='./datasets', train=True, download=True, transform=transform)
        testset = torchvision.datasets.CIFAR10(root='./datasets', train=False, download=True, transform=transform)
        num_classes = 10
        inputs=3

    elif(dataset == 'CIFAR100'):
        trainset = torchvision.datasets.CIFAR100(root='./datasets', train=True, download=True, transform=transform)
        testset = torchvision.datasets.CIFAR100(root='./datasets', train=False, download=True, transform=transform)
        num_classes = 100
        inputs = 3
        
    elif(dataset == 'MNIST'):
        trainset = torchvision.datasets.MNIST(root='./datasets', train=True, download=True, transform=transform)
        testset = torchvision.datasets.MNIST(root='./datasets', train=False, download=True, transform=transform)
        num_classes = 10
        inputs = 1

    return trainset, testset, inputs, num_classes

def getDataloader(trainset, testset, valid_size, batch_size, num_workers):
    num_train = len(trainset)
    indices = list(range(num_train))
    np.random.shuffle(indices)
    split = int(np.floor(valid_size * num_train))
    train_idx, valid_idx = indices[split:], indices[:split]

    train_sampler = SubsetRandomSampler(train_idx)
    valid_sampler = SubsetRandomSampler(valid_idx)

    train_loader = torch.utils.data.DataLoader(trainset, batch_size=batch_size,
        sampler=train_sampler, num_workers=num_workers)
    valid_loader = torch.utils.data.DataLoader(trainset, batch_size=batch_size, 
        sampler=valid_sampler, num_workers=num_workers)
    test_loader = torch.utils.data.DataLoader(testset, batch_size=batch_size, 
        num_workers=num_workers)

    return train_loader, valid_loader, test_loader
