
from pycaret.datasets import get_data

data = get_data('france')
from pycaret.arules import *

s = setup(data = data, transaction_id = 'InvoiceNo', item_id = 'Description')

arules = create_model(metric='confidence', threshold=0.5, min_support=0.05)
plot_model(arules, plot = '2d')
plot_model(arules, plot = '3d')
