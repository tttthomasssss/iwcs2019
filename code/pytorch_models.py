from torch import nn


ACTIVATIONS = {
	'tanh': nn.Tanh,
	'sigmoid': nn.Sigmoid,
	'relu': nn.ReLU,
	'prelu': nn.PReLU,
	'selu': nn.SELU,
	'elu': nn.ELU
}


class FeedforwardLayer(nn.Module):
	def __init__(self, input_dim, output_dim, activation, dropout_ratio):
		super(FeedforwardLayer, self).__init__()
		self.feedforward = nn.Sequential(
			nn.Linear(input_dim, output_dim),
			ACTIVATIONS[activation](),
			nn.Dropout(p=dropout_ratio)
		)

	def forward(self, sequence):
		return self.feedforward(sequence)


class InflectionFeedforward(nn.Module):
	def __init__(self, input_dim, num_layers, hidden_size, activations, dropout_ratios):
		super(InflectionFeedforward, self).__init__()
		self.num_layers = num_layers

		if (num_layers > 1 and not isinstance(hidden_size, list)):
			hidden_size = [hidden_size] * num_layers
		if (num_layers > 1 and not isinstance(activations, list)):
			activations = [activations] * num_layers
		if (num_layers > 1 and not isinstance(dropout_ratios, list)):
			dropout_ratios = [dropout_ratios] * num_layers

		self.forward_layer_1 = FeedforwardLayer(input_dim=input_dim, output_dim=hidden_size[0],
												activation=activations[0], dropout_ratio=dropout_ratios[0])

		for i, (size, activation, dropout_ratio) in enumerate(zip(hidden_size[1:], activations[1:], dropout_ratios[1:]), 1):
			layer = FeedforwardLayer(input_dim=hidden_size[i-1], output_dim=input_dim if size == 'XXX' else size,
									 activation=activation, dropout_ratio=dropout_ratio)
			setattr(self, f'forward_layer_{i+1}', layer)

	def forward(self, infinitives):
		for i in range(self.num_layers):
			infinitives = getattr(self, f'forward_layer_{i+1}')(infinitives)

		return infinitives
