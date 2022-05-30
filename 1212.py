# -*- coding: utf-8 -*-

import numpy as np
      
def feature_normalization(data): # 10 points
    # parameter 
    feature_num = data.shape[1]
    data_point = data.shape[0]
    
    # you should get this parameter correctly
    normal_feature = np.zeros([data_point, feature_num])
    mu = np.zeros([feature_num])
    std = np.zeros([feature_num])
    
    # your code here
    for i in range (0,feature_num):
        mu[i]=np.mean(data[:,i]) #각 feature 별 평균을 구함
        std[i]=np.std(data[:,i]) #각  feature 별 표준편차를 구함

    for i in range(0,feature_num):
        for j in range(0,data_point):
            normal_feature[j][i]=(data[j][i]-mu[i])/std[i] # 주어진 data들을 정규화하는 과정을 거침.
    # end

    return normal_feature
        
def split_data(data, label, split_factor):
    return  data[:split_factor], data[split_factor:], label[:split_factor], label[split_factor:]

def get_normal_parameter(data, label, label_num): # 20 points
    # parameter
    feature_num = data.shape[1]

    # you should get this parameter correctly    
    mu = np.zeros([label_num,feature_num])
    sigma = np.zeros([label_num,feature_num])

    # your code here
    for i in range(label_num):
        label_temp = np.where(label == i) # 데이터가 랜덤하게 섞여있기 때문에 동일한 label을 갖는 data의 index를 찾아줌
        label_match = label_temp[0] # index array 값을 저장
        for j in range(feature_num):
            target = [] # index에 해당하는 feature를 저장하기 위한 리스트 초기화
            for k in range(len(label_match)): # 하나의 label에서 4개의 feature 값들을 구함
                target.append(data[label_match[k]][j]) # 헤당 index의 값을 리스트에 저장함
            mu[i][j] = np.mean(target) #저장한 값들의 평균을 구함
            sigma[i][j] = np.std(target) #저장한 값들의 표준편차를 구함
    # end
    
    return mu, sigma

def get_prior_probability(label, label_num): # 10 points
    # parameter
    data_point = label.shape[0]
    
    # you should get this parameter correctly
    prior = np.zeros([label_num])
    
    # your code here
    for i in range(label_num):
        a = np.where(label == i)
        prior[i] = len(a[0])  # 해당하는 label의 개수를 구해서 prior 리스트에 저장함
    for i in range (label_num):
        prior[i]/=data_point # 확률을 구해야하므로 각 label의 개수를 총 label의 개수로 나눠줌
    # end
    return prior

def Gaussian_PDF(x, mu, sigma): # 10 points
    # calculate a probability (PDF) using given parameters
    # you should get this parameter correctly
    pdf = 0
    
    # your code here
    pdf = (1 / np.sqrt(2*np.pi*sigma**2)) * np.exp(-(x-mu)**2 / (2*sigma**2)) #가우시안 분포 확률의 수식을 표현하였음
    # end
    
    return pdf

def Gaussian_Log_PDF(x, mu, sigma): # 10 points
    # calculate a probability (PDF) using given parameters
    # you should get this parameter correctly
    log_pdf = 0
    
    # your code here
    log_pdf = np.log(1 / np.sqrt(2*np.pi*sigma**2)) * np.exp(-(x-mu)**2 / (2*sigma**2)) #기존 가우시안 분포 확률 값에 ln을 취해준 결과임. 
    # end
    
    return log_pdf

def Gaussian_NB(mu, sigma, prior, data): # 40 points
    # parameter
    data_point = data.shape[0]
    label_num = mu.shape[0]
    
    # you should get this parameter correctly   
    likelihood = np.zeros([data_point, label_num])
    posterior = np.zeros([data_point, label_num])
    ## evidence can be ommitted because it is a constant
    
    # your code here
        ## Function Gaussian_PDF or Gaussian_Log_PDF should be used in this section
    for i in range (label_num):
        for j in range (data_point): #해당 likelihood 값을 구할 때 로그 값을 사용하지 않고 일반 가우시안 확률 값을 곱하는 것을 통해 구하였음. 이 때 feature들이 label 0,1,2일 확률을 구해주어야 함.
            likelihood[j][i]=Gaussian_PDF(data[j][0],mu[i][0],sigma[i][0])*Gaussian_PDF(data[j][1],mu[i][1],sigma[i][1])*Gaussian_PDF(data[j][2],mu[i][2],sigma[i][2])*Gaussian_PDF(data[j][3],mu[i][3],sigma[i][3])

    for i in range (data_point):
        for j in range (label_num):
            posterior[i][j]=likelihood[i][j]*prior[j] #구한 likelihood 값에 선험적 확률을 곱하면 posterior 값이 됨. 원래는 evidence 값을 나눠줘야 하지만 이는 무시해도 상관 없음
    # end
    return posterior

def classifier(posterior):
    data_point = posterior.shape[0]
    prediction = np.zeros([data_point])
    
    prediction = np.argmax(posterior, axis=1)
    
    return prediction
        
def accuracy(pred, gnd):
    data_point = len(gnd)
    
    hit_num = np.sum(pred == gnd)

    return (hit_num / data_point) * 100, hit_num

    ## total 100 point you can get 