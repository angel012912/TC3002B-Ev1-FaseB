from keras.models import load_model

model = load_model('/Users/angel/Documents/Tec/8vo Sem/TC3002B-Ev1-FaseB/Model/new_weights.h5')
print(model.summary())