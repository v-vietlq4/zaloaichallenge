from .base_options import BaseOptions


class TrainOptions(BaseOptions):
    def initialize(self, parser):
        parser = BaseOptions.initialize(self, parser)

        # For dataset configurations
        # Paths
        parser.add_argument(
            '--train_root', help='root folder containing images for training')
        parser.add_argument(
            '--train_list', help='.txt file containing training image list')

        # Augmentations
        parser.add_argument('--crop_width', type=int,
                            default=1024, help='cropping width during training')
        parser.add_argument('--crop_height', type=int,
                            default=512, help='cropping height during training')
        parser.add_argument('--rotate', type=int, default=20,
                            help='angle for rotation')
        parser.add_argument('--color_aug_ratio', type=float, default=0.3,
                            help='ratio of images applied color augmentation')
        parser.add_argument('--only_flip', action='store_true',
                            help='apply only left-right flipping in augmentation')
        parser.add_argument('--use_color_aug', action='store_true',
                            help='apply color jitter in augmentation')

        parser.add_argument('--resume', type=str,
                            help='resume path for continue training (.ckpt)')

        parser.add_argument('--max_epoch', type=int,
                            default=1000, help='maximum epochs')

        parser.add_argument('--optimizer', type=str, default='adam',
                            help='optimizer to be used: adam, sgd')
        parser.add_argument('--lr', type=float, default=0.001,
                            help='initial learning rate for optimizer')
        parser.add_argument('--weight_decay', type=float,
                            default=0.0005, help='momentum factor for optimizer')
        # adam
        parser.add_argument('--beta1', type=float,
                            default=0.5, help='momentum term of adam')
        # sgd
        parser.add_argument('--momentum', type=float,
                            default=0.9, help='momentum factor for sgd')

        # learning rate scheduler
        parser.add_argument('--lr_policy', type=str, default='step',
                            help='learning rate policy: exp, step, multi_step')
        parser.add_argument('--lr_step', type=int, default=10,
                            help='step_size for step lr scheduler')
        parser.add_argument('--lr_milestones', metavar='N', nargs="+",
                            type=int, help='milestones for multi step lr scheduler')
        parser.add_argument('--lr_gamma', type=float,
                            default=0.9, help='gamma factor for lr_scheduler')

        # For early stopping
        parser.add_argument('--patience', type=int, default=-1,
                            help='stops training after a number of epochs without improvement')

        # Choosing loss functions
        parser.add_argument('--loss', nargs="+", type=str, default=[
                            'ohem', 'tversky'], help='loss options for training: ce, ohem, tversky')
        parser.add_argument('--use_aux', action='store_true',
                            help='apply auxilary loss while training. Currently use with OCR net')
        parser.add_argument('--ocr_alpha_loss', type=float,
                            default=0.4, help='weight for OCR aux loss')

        return parser

    # def parse(self):
    #     self.opt = super().parse()

    #     self.opt.lr_milestones =
