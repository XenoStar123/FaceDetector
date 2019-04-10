import unittest
from mtcnn.train.train_net import Trainer

class TestTrain(unittest.TestCase):

    def test_train_pnet(self):
        trainer = Trainer('pnet', device='cuda:0')
        trainer.train(100, 256, './output/test')
    

if __name__ == "__main__":
    unittest.main()

    