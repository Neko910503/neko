import tensorflow as tf
import numpy as np

data = [] #處存樣本集的清單
for i in range(1000): #循環採樣100個點
  x = np.random.uniform(-10.,10.) #隨機採樣輸入x
  esp = np.random.normal(0.,0.01) #採樣高斯雜訊
  y = 1.477 * + 0.0898 + esp
  data.append([x,y]) #處存樣本點
data = np.array(data) #轉為2D陣列

def mse(b,w,points):
  # 根據目前的w,b參數計算方均方誤差損失
  totalError = 0 
  for i in range(0,len(points)): #循環反覆運算所有點
    x = points[i,0] #獲得i號點的輸入x
    y = points[i,1] #獲得i號點的輸入y
    # 計算的平方，並累加
    totalError += (y - (w*x+b)) ** 2

  return totalError / float(len(points))  

def step_gradient(b_current, w_current, points, lr):
  b_gradient = 0
  w_gradient = 0
  M = float(len(points)) #總樣本數量
  for i in range(len(points)):
    x = points[i,0]
    y = points[i,1]
    b_gradient += (2/M) * ((w_current*x+b_current)-y)
    w_gradient += (2/M) * x *((w_current * x + b_current)-y)
  # 根據梯度下降演算法更新w',b',其中lr為學習效率
  new_b = b_current - (lr * b_gradient)
  new_w = w_current - (lr * w_gradient)   

  return [new_b, new_w]

def gradient_descent(points,starting_b,starting_w,lr,num_iterations):
  # 循環更新w,b多次
  b = starting_b #b 的初始數值
  w = starting_w #w的初始數值

  for step in range(num_iterations):
    # 計算梯度並更新一次
    b,w = step_gradient(b,w,np.array(points),lr)
    loss = mse(b,w,points) #計算目前的均方誤差，用於監控訓練速度
    if step % 50 == 0: #列印誤差和即時的b,w值
      print(f"iterations:{step},loss:{loss},w:{w},b:{b}")

  return [b,w]    #傳回最後的b,w

def main():
  # 載入訓練集資料，這些資料透過真實模型增加觀察誤差採樣獲得的
  lr = 0.01 #學習率
  initial_b = 0 # 初始化 b 為 0
  initial_w = 0 # 初始化 w 為 0`
  num_iterations = 1000
  # 訓練最佳化 1000 次，傳回最佳 W* , b* 和訓練 loss 的下降過程
  [b,w] = gradient_descent(data, initial_b, initial_w, lr, num_iterations)
  loss = mse(b,w,data) #計算最佳數值解 w,b 上的均方誤差
  
  print(f"Final loss:{loss}, w:{w} ,b:{b}")

if __name__ == "__main__":
  main()