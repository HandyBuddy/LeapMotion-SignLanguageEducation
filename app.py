import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import string
import json
import leap_two_hand
import leap_one_hand
#import threading
from flask import Flask, render_template, jsonify, request

class_name=""

app = Flask(__name__,
            static_folder='flask/static',
            template_folder='flask/templates')

def to_tensor(x):
    data_list = list(map(float, x.split()))
    arr = np.array(data_list)
    length = len(arr)
    max_length = 7982
    padded_data = np.zeros(max_length)

    if length < max_length:
        padded_data[0:length] = arr[0:length]
    else:
        padded_data = arr[0:max_length]
    
    return torch.from_numpy(padded_data.astype(np.float32)), torch.tensor(length)

# Hyperparameters
input_size = 26
sequence_length = 307 # 7982(max_length)/26
hidden_size = 256
num_layers = 2
num_classes = 35
learning_rate=0.001

# create a LSTM
class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, num_classes):
        super(LSTM, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size*sequence_length, num_classes)
    
    def forward(self, x, l):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size)
        out_pack, (ht, ct) = self.lstm(x, (h0, c0))
        out_pack = out_pack.reshape(out_pack.shape[0], -1)
        out = self.fc(out_pack)
        return out

def load_checkpoint(checkpoint):
    model.load_state_dict(checkpoint['state_dict'])
    optimizer.load_state_dict(checkpoint['optimizer'])
    model.eval()

# Initialize network
model = LSTM(input_size=input_size, hidden_size=hidden_size, num_layers=num_layers, num_classes=num_classes)

# initialize optimizer
parameters = filter(lambda p: p.requires_grad, model.parameters())
optimizer = torch.optim.Adam(parameters, lr=learning_rate)

load_checkpoint(torch.load("my_checkpoint.pth.tar"))

sl_class_index = json.load(open('./sl_class_index.json'))

def getTwoHandPred():
    global class_name
    data = leap_two_hand.two_hand_data
    tensor = to_tensor(data)
    x = tensor[0]
    l = tensor[1]
    x = x.view(-1, 26).unsqueeze(0)
    _, y_hat = model.forward(x, l).max(1)
    pred_idx = str(y_hat.item())
    class_name = sl_class_index[pred_idx]
    
def getOneHandPred():
    global class_name
    data = leap_one_hand.one_hand_data
    tensor = to_tensor(data)
    x = tensor[0]
    l = tensor[1]
    x = x.view(-1, 26).unsqueeze(0)
    _, y_hat = model.forward(x, l).max(1)

    pred_idx = str(y_hat.item())
    class_name = sl_class_index[pred_idx]

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/learning_onehand')
def onehand_words():
    return render_template("onehand_words.html")

@app.route('/learning_twohand')
def twohand_words():
    return render_template("twohand_words.html")

@app.route('/onehand_first')
def onehand_first():
    return render_template("onehand_first.html")

@app.route('/onehand_hobby')
def onehand_hobby():
    return render_template("onehand_hobby.html")

@app.route('/onehand_what')
def onehand_what():
    return render_template("onehand_what.html")

@app.route('/onehand_like')
def onehand_like():
    return render_template("onehand_like.html")

@app.route('/onehand_dog')
def onehand_dog():
    return render_template("onehand_dog.html")

@app.route('/onehand_thesedays')
def onehand_thesedays():
    return render_template("onehand_thesedays.html")

@app.route('/onehand_eat')
def onehand_eat():
    return render_template("onehand_eat.html")

@app.route('/onehand_go')
def onehand_go():
    return render_template("onehand_go.html")

@app.route('/onehand_sick')
def onehand_sick():
    return render_template("onehand_sick.html")

@app.route('/onehand_cough')
def onehand_cough():
    return render_template("onehand_cough.html")

@app.route('/onehand_ill')
def onehand_ill():
    return render_template("onehand_ill.html")

@app.route('/onehand_be')
def onehand_be():
    return render_template("onehand_be.html")

@app.route('/onehand_enough')
def onehand_enough():
    return render_template("onehand_enough.html")

@app.route('/onehand_and')
def onehand_and():
    return render_template("onehand_and.html")

@app.route('/onehand_come')
def onehand_come():
    return render_template("onehand_come.html")

@app.route('/onehand_yes')
def onehand_yes():
    return render_template("onehand_yes.html")

@app.route('/onehand_twodaysafter')
def onehand_twodaysafter():
    return render_template("onehand_twodaysafter.html")

@app.route('/twohands_hi')
def twohands_hi():
    return render_template("twohands_hi.html")

@app.route('/twohands_meet')
def twohands_meet():
    return render_template("twohands_meet.html")

@app.route('/twohands_nicetomeet')
def twohands_nicetomeet():
    return render_template("twohands_nicetomeet.html")

@app.route('/twohands_readingbook')
def twohands_readingbook():
    return render_template("twohands_readingbook.html")

@app.route('/twohands_animal')
def twohands_animal():
    return render_template("twohands_animal.html")

@app.route('/twohands_longtimenosee')
def twohands_longtimenosee():
    return render_template("twohands_longtimenosee.html")

@app.route('/twohands_busy')
def twohands_busy():
    return render_template("twohands_busy.html")

@app.route('/learning_twohand/twohands_end')
def twohands_end():
    return render_template("twohands_end.html")

@app.route('/learning_twohand/twohands_yet')
def twohands_yet():
    return render_template("twohands_yet.html")

@app.route('/twohands_together')
def twohands_together():
    return render_template("twohands_together.html")

@app.route('/learning_twohand/twohands_noodle')
def twohands_noodle():
    return render_template("twohands_noodle.html")

@app.route('/learning_twohand/twohands_cold')
def twohands_cold():
    return render_template("twohands_cold.html")

@app.route('/twohands_different')
def twohands_different():
    return render_template("twohands_different.html")

@app.route('/learning_twohand/twohands_state')
def twohands_state():
    return render_template("twohands_state.html")

@app.route('/learning_twohand/twohands_no')
def twohands_no():
    return render_template("twohands_no.html")

@app.route('/learning_twohand/twohands_medicine')
def twohands_medicine():
    return render_template("twohands_medicine.html")

@app.route('/learning_twohand/twohands_rest')
def twohands_rest():
    return render_template("twohands_rest.html")

@app.route('/twohands_favor')
def twohands_favor():
    return render_template("twohands_favor.html")
    
@app.route('/randomgame')
def randomgame():
    return render_template("randomgame.html")
    
@app.route('/gamestart1')
def gamestart1():
    return render_template("gamestart1.html")

@app.route('/gamestart2')
def gamestart2():
    return render_template("gamestart2.html")


@app.route('/predict_two_hand', methods=['GET'])
def predict_two_hand():
    leap_two_hand.main()
    getTwoHandPred()
    return class_name
    

@app.route('/predict_one_hand')
def predict_one_hand():
    leap_one_hand.main()
    getOneHandPred()
    return class_name

if __name__ == '__main__':
    app.run(debug=True)
    
