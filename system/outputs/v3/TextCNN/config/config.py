class Config:
    def __init__(self, learning_rate, batch_size, num_epochs, embedding_dim, kernel_sizes, max_length,
                 save_every_n_epoch, train, test, output_dir, gpu, train_log_per_k_batch, random_seed):
        self.learning_rate = learning_rate
        self.batch_size = batch_size
        self.num_epochs = num_epochs
        self.embedding_dim = embedding_dim
        self.kernel_sizes = kernel_sizes
        self.max_length = max_length
        self.save_every_n_epoch = save_every_n_epoch
        self.train = train
        self.test = test
        self.output_dir = output_dir
        self.gpu = gpu
        self.train_log_per_k_batch = train_log_per_k_batch
        self.random_seed = random_seed