import numpy as np

class CNN:
    def __init__(self, input_shape, num_filters, filter_size, num_classes):
        self.input_shape = input_shape # Ex: (altura, largura) para escala de cinza
        self.num_filters = num_filters
        self.filter_size = filter_size
        self.num_classes = num_classes
        
        # Inicializa os filtros da camada convolucional
        self.filters = np.random.randn(num_filters, filter_size, filter_size) / (filter_size**2)

        # Dimensões de saída da camada convolucional (sem padding)
        self.conv_output_height = input_shape[0] - filter_size + 1
        self.conv_output_width = input_shape[1] - filter_size + 1 # Assumindo input_shape = (altura, largura)

        # Dimensões padrão para pooling (usadas para calcular flattened_size no __init__)
        self.pool_size_default = 2
        self.pool_stride_default = 2

        # Calcula as dimensões de saída do pooling com base nos defaults
        self.pool_output_height = self.conv_output_height // self.pool_stride_default
        self.pool_output_width = self.conv_output_width // self.pool_stride_default

        # Calcula o tamanho do vetor após o achatamento
        self.flattened_size = num_filters * (self.pool_output_height * self.pool_output_width)

        # Inicializa os pesos da camada totalmente conectada
        self.weights = np.random.randn(self.flattened_size, num_classes) / 100
        self.bias = np.zeros(num_classes)

    def convolution(self, input_image):
        # A entrada para a convolução é uma imagem 2D (altura, largura)
        output_feature_maps = np.zeros((self.num_filters, self.conv_output_height, self.conv_output_width))

        for f in range(self.num_filters): # Itera por cada filtro
            current_filter = self.filters[f]
            for i in range(self.conv_output_height):
                for j in range(self.conv_output_width):
                    # Extrai a região da imagem para aplicar o filtro
                    region = input_image[i : i + self.filter_size, j : j + self.filter_size]
                    # Realiza o produto elemento a elemento e soma
                    conv_result = np.sum(region * current_filter)
                    output_feature_maps[f, i, j] = conv_result
        return output_feature_maps

    def pooling(self, input_feature_map, pool_size=2, stride=2):
        # Este método recebe UM ÚNICO mapa de características 2D (altura, largura)
        map_height, map_width = input_feature_map.shape

        # Calcula as dimensões de saída para este mapa específico com os pool_size e stride fornecidos
        output_height = (map_height - pool_size) // stride + 1
        output_width = (map_width - pool_size) // stride + 1

        pooled_map = np.zeros((output_height, output_width))

        for i in range(output_height):
            for j in range(output_width):
                start_row = i * stride
                end_row = start_row + pool_size
                start_col = j * stride
                end_col = start_col + pool_size

                region = input_feature_map[start_row:end_row, start_col:end_col]
                max_value = np.max(region)
                pooled_map[i, j] = max_value

        return pooled_map

    def forward(self, input_image):
        # Passagem pela camada convolucional ---
        conv_output = self.convolution(input_image)
        pooled_output_collection = np.zeros((self.num_filters, self.pool_output_height, self.pool_output_width))

        for f in range(self.num_filters):
            # Aplica o método `pooling` a cada mapa de características
            # usando os pool_size e stride padrão definidos no __init__
            pooled_output_collection[f] = self.pooling(
                conv_output[f], self.pool_size_default, self.pool_stride_default
            )

        flattened_output = pooled_output_collection.flatten()

        logits = np.dot(flattened_output, self.weights) + self.bias

        return np.argmax(logits) # Retorna o índice da classe com o maior logit


# Test Case para ajustar entradas e parâmetros
np.random.seed(40)  # Garante resultados consistentes
input_image = np.array([[1, 2, 3,4], [5, 6, 7,8], [9, 10, 11,12], [13,14,15,16]])  # Imagem 3x3 fixa
cnn = CNN(input_shape=(4, 4), num_filters=2, filter_size=2, num_classes=3)

# Configurando filtros e pesos fixos para garantir resultado determinístico
cnn.filters = np.random.randn(2, 2, 2)
cnn.weights = np.random.randn(2 * 1, 3) / 100  # Ajuste do tamanho dos pesos

# Classe prevista
predicted_class = cnn.forward(input_image)
print("Classe prevista:", predicted_class)