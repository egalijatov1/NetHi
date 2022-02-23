from PIL import Image

#load images for drawing
plusImage = Image.open('images/plus.png')
minusImage = Image.open('images/minus.png')
starImage = Image.open('images/star_black.png')
default_stylesheet = [
    # Group selectors
    {
        'selector': 'node',
        'style': {
            'content': 'data(label)',
            'border-width': 1,
            'border-color': '#787878',
        }
    },
    {
      'selector':'edge',
      'style':{
          'width':1,
          'line-color':'#4d4d4d',
      }
    },
    # Class selectors
     {
        'selector': '.star',
        'style': {
            'background-image': starImage,
            'background-width': '50%',
            'background-height': '50%',
        }
    },
    {
        'selector': '.plus',
        'style': {
            'background-image': plusImage,
            'background-width': '60%',
            'background-height': '60%',
        }
    },
    {
        'selector': '.minus',
        'style': {
            'background-image': minusImage,
            'background-width': '60%',
            'background-height': '10%',
        }
    },


    {
        'selector': '.leaf',
        'style': {
        }
    },
    {
        'selector': '.important',
        'style': {
            'shape':'star',
            'border-width': 5,
            'border-color': '#000',
            'width':'60px',
            'height':'60px'
        }
    },
    {
        'selector': '[num_children >= 25]',
        'style': {
            'width': '100px',
            'height': '100px'

        }
    },

    {
        'selector': '[num_children >= 100]',
        'style': {
            'width': '200px',
            'height': '200px'

        }
    },
    {
        'selector': '[num_children >= 150]',
        'style': {
            'width': '300px',
            'height': '300px'

        }
    },
    {
        'selector': '[id *= "virt"]',
        'style': {
            'shape':'diamond',
            'border-width': 4,
            'border-color': '#787878',
        }
    },
    {
        'selector': '.main',
        'style': {
            'background-color': '#F5F5F5',
            'border-width': 1,
            'border-color': '#000',
            'shape':'diamond',
        }
    },

    {
	'selector': '.0',
        'style':{
            'background-color':'#42d4f4'
        }
    },
    {
        'selector': '.1',
        'style':{
            'background-color':'#911eb4'
        }
    },
    {
        'selector': '.2',
        'style':{
            'background-color':'#f58231'
        }
    },
    {
        'selector': '.3',
        'style':{
            'background-color':'#4363d8'
        }
    },
    {
        'selector': '.4',
        'style':{
            'background-color':'#ffe119'
        }
    },
    {
        'selector': '.5',
        'style':{
            'background-color':'#3cb44b'
        }
    },
    {
        'selector': '.6',
        'style':{
            'background-color':'#e6194B'
        }
    },
    {
        'selector': '.7',
        'style':{
            'background-color':'#bfef45'
        }
    },
    {
        'selector': '.8',
        'style':{
            'background-color':'#000075'
        }
    },
    {
        'selector': '.9',
        'style':{
            'background-color':'#fabed4'
        }
    },
    {
        'selector': '.10',
        'style':{
            'background-color':'#800000'
        }
    },
    {
        'selector': '.11',
        'style':{
            'background-color':'#f032e6'
        }
    },
    {
        'selector': '.12',
        'style':{
            'background-color':'#aaffc3'
        }
    },
    {
        'selector': '.13',
        'style':{
            'background-color':'#ffd8b1'
        }
    },
    {
        'selector': '.14',
        'style':{
            'background-color':'#dcbeff'
        }
    },
    {
        'selector': '.15',
        'style':{
            'background-color':'#469990'
        }
    },
    {
        'selector': '.16',
        'style':{
            'background-color':'#fffac8'
        }
    },
    {
        'selector': '.17',
        'style':{
            'background-color':'#808000'
        }
    },
    {
        'selector': '.18',
        'style':{
            'background-color':'#f3e100'
        }
    },
    {
        'selector': '.19',
        'style':{
            'background-color':'#ffb900'
        }
    },
    {
        'selector': '.20',
        'style':{
            'background-color':'#dc0000'
        }
    },
    {
        'selector': '.21',
        'style':{
            'background-color':'#ff3900'
        }
    },
    {
        'selector': '.22',
        'style':{
            'background-color':'#fe0000'
        }
    },
    {
        'selector': '.23',
        'style':{
            'background-color':'#cc0c0c'
        }
    },
    {
        'selector': '.24',
        'style':{
            'background-color':'#00aaa0'
        }
    },
    {
        'selector': '.25',
        'style':{
            'background-color':'#009dcf'
        }
    },
    {
        'selector': '.26',
        'style':{
            'background-color':'#00b600'
        }
    },
    {
        'selector': '.27',
        'style':{
            'background-color':'#120015'
        }
    },
    {
        'selector': '.28',
        'style':{
            'background-color':'#ffa500'
        }
    },
    {
        'selector': '.29',
        'style':{
            'background-color':'#70007f'
        }
    },
    {
        'selector': '.30',
        'style':{
            'background-color':'#00a45d'
        }
    },
    {
        'selector': '.31',
        'style':{
            'background-color':'#00a900'
        }
    },
    {
        'selector': '.32',
        'style':{
            'background-color':'#f10000'
        }
    },
    {
        'selector': '.33',
        'style':{
            'background-color':'#cf0000'
        }
    },
    {
        'selector': '.34',
        'style':{
            'background-color':'#cbf900'
        }
    },
    {
        'selector': '.35',
        'style':{
            'background-color':'#009b12'
        }
    },
    {
        'selector': '.36',
        'style':{
            'background-color':'#ff5d00'
        }
    },
    {
        'selector': '.37',
        'style':{
            'background-color':'#4d00a0'
        }
    },
    {
        'selector': '.38',
        'style':{
            'background-color':'#001cdd'
        }
    },
    {
        'selector': '.39',
        'style':{
            'background-color':'#83ff00'
        }
    },
    {
        'selector': '.40',
        'style':{
            'background-color':'#1dff00'
        }
    },
    {
        'selector': '.41',
        'style':{
            'background-color':'#00e700'
        }
    },
    {
        'selector': '.42',
        'style':{
            'background-color':'#ff2000'
        }
    },
    {
        'selector': '.43',
        'style':{
            'background-color':'#002edd'
        }
    },
    {
        'selector': '.44',
        'style':{
            'background-color':'#0000d5'
        }
    },
    {
        'selector': '.45',
        'style':{
            'background-color':'#009e27'
        }
    },
    {
        'selector': '.46',
        'style':{
            'background-color':'#009c00'
        }
    },
    {
        'selector': '.47',
        'style':{
            'background-color':'#008ddd'
        }
    },
    {
        'selector': '.48',
        'style':{
            'background-color':'#00a247'
        }
    },
    {
        'selector': '.49',
        'style':{
            'background-color':'#004add'
        }
    },
    {
        'selector': '.50',
        'style':{
            'background-color':'#f7d900'
        }
    },
    {
        'selector': '.51',
        'style':{
            'background-color':'#0200a9'
        }
    },
    {
        'selector': '.52',
        'style':{
            'background-color':'#00aaa8'
        }
    },
    {
        'selector': '.53',
        'style':{
            'background-color':'#00aa8d'
        }
    },
    {
        'selector': '.54',
        'style':{
            'background-color':'#3700a3'
        }
    },
    {
        'selector': '.55',
        'style':{
            'background-color':'#00e100'
        }
    },
    {
        'selector': '.56',
        'style':{
            'background-color':'#e30000'
        }
    },
    {
        'selector': '.57',
        'style':{
            'background-color':'#00fc00'
        }
    },
    {
        'selector': '.58',
        'style':{
            'background-color':'#1700a7'
        }
    },
    {
        'selector': '.59',
        'style':{
            'background-color':'#3aff00'
        }
    },
    {
        'selector': '.60',
        'style':{
            'background-color':'#66ff00'
        }
    },
    {
        'selector': '.61',
        'style':{
            'background-color':'#d7f500'
        }
    },
    {
        'selector': '.62',
        'style':{
            'background-color':'#870098'
        }
    },
    {
        'selector': '.63',
        'style':{
            'background-color':'#2e0035'
        }
    },
    {
        'selector': '.64',
        'style':{
            'background-color':'#0066dd'
        }
    },
    {
        'selector': '.65',
        'style':{
            'background-color':'#0000b5'
        }
    },
    {
        'selector': '.66',
        'style':{
            'background-color':'#00d400'
        }
    },
    {
        'selector': '.67',
        'style':{
            'background-color':'#000000'
        }
    },
    {
        'selector': '.68',
        'style':{
            'background-color':'#cc2c2c'
        }
    },
    {
        'selector': '.69',
        'style':{
            'background-color':'#0077dd'
        }
    },
    {
        'selector': '.70',
        'style':{
            'background-color':'#ff8100'
        }
    },
    {
        'selector': '.71',
        'style':{
            'background-color':'#0000c9'
        }
    },
    {
        'selector': '.72',
        'style':{
            'background-color':'#0000bd'
        }
    },
    {
        'selector': '.73',
        'style':{
            'background-color':'#d90000'
        }
    },
    {
        'selector': '.74',
        'style':{
            'background-color':'#f1e700'
        }
    },
    {
        'selector': '.75',
        'style':{
            'background-color':'#0099db'
        }
    },
    {
        'selector': '.76',
        'style':{
            'background-color':'#00a87d'
        }
    },
    {
        'selector': '.77',
        'style':{
            'background-color':'#5d006a'
        }
    },
    {
        'selector': '.78',
        'style':{
            'background-color':'#dff200'
        }
    },
    {
        'selector': '.79',
        'style':{
            'background-color':'#00be00'
        }
    },
    {
        'selector': '.80',
        'style':{
            'background-color':'#ebee00'
        }
    },
    {
        'selector': '.81',
        'style':{
            'background-color':'#7e008e'
        }
    },
    {
        'selector': '.82',
        'style':{
            'background-color':'#00a7b3'
        }
    },
    {
        'selector': '.83',
        'style':{
            'background-color':'#00f400'
        }
    },
    {
        'selector': '.84',
        'style':{
            'background-color':'#cc5c5c'
        }
    },
    {
        'selector': '.85',
        'style':{
            'background-color':'#00ef00'
        }
    },
    {
        'selector': '.86',
        'style':{
            'background-color':'#cccccc'
        }
    },
    {
        'selector': '.87',
        'style':{
            'background-color':'#00aa9a'
        }
    },
    {
        'selector': '.88',
        'style':{
            'background-color':'#fad400'
        }
    },
    {
        'selector': '.89',
        'style':{
            'background-color':'#c3fb00'
        }
    },
    {
        'selector': '.90',
        'style':{
            'background-color':'#cc7c7c'
        }
    },
    {
        'selector': '.91',
        'style':{
            'background-color':'#d50000'
        }
    },
    {
        'selector': '.92',
        'style':{
            'background-color':'#0000dd'
        }
    },
    {
        'selector': '.93',
        'style':{
            'background-color':'#6d009c'
        }
    },
    {
        'selector': '.94',
        'style':{
            'background-color':'#eb0000'
        }
    },
    {
        'selector': '.95',
        'style':{
            'background-color':'#d30000'
        }
    },
    {
        'selector': '.96',
        'style':{
            'background-color':'#00cc00'
        }
    },
    {
        'selector': '.97',
        'style':{
            'background-color':'#00a4bb'
        }
    },
    {
        'selector': '.98',
        'style':{
            'background-color':'#fecc00'
        }
    },
    {
        'selector': '.99',
        'style':{
            'background-color':'#00a100'
        }
    },
    {
	'selector': '.0e',
	'style':{
            'line-color':'#42d4f4',
            'width':1
        }
    },
    {
        'selector': '.1e',
        'style':{
            'line-color':'#911eb4',
            'width':1
        }
    },
    {
        'selector': '.2e',
        'style':{
            'line-color':'#f58231',
            'width':1
        }
    },
    {
        'selector': '.3e',
        'style':{
            'line-color':'#4363d8',
            'width':1
        }
    },
    {
        'selector': '.4e',
        'style':{
            'line-color':'#ffe119',
            'width':1
        }
    },
    {
        'selector': '.5e',
        'style':{
            'line-color':'#3cb44b',
            'width':1
        }
    },
    {
        'selector': '.6e',
        'style':{
            'line-color':'#e6194B',
            'width':1
        }
    },
    {
        'selector': '.7e',
        'style':{
            'line-color':'#bfef45',
            'width':1
        }
    },
    {
        'selector': '.8e',
        'style':{
            'line-color':'#000075',
            'width':1
        }
    },
    {
        'selector': '.9e',
        'style':{
            'line-color':'#fabed4',
            'width':1
        }
    },
    {
        'selector': '.10e',
        'style':{
            'line-color':'#800000',
            'width':1
        }
    },
    {
        'selector': '.11e',
        'style':{
            'line-color':'#f032e6',
            'width':1
        }
    },
    {
        'selector': '.12e',
        'style':{
            'line-color':'#aaffc3',
            'width':1
        }
    },
    {
        'selector': '.13e',
        'style':{
            'line-color':'#ffd8b1',
            'width':1
        }
    },
    {
        'selector': '.14e',
        'style':{
            'line-color':'#dcbeff',
            'width':1
        }
    },
    {
        'selector': '.15e',
        'style':{
            'line-color':'#469990',
            'width':1
        }
    },
    {
        'selector': '.16e',
        'style':{
            'line-color':'#fffac8',
            'width':1
        }
    },
    {
        'selector': '.17e',
        'style':{
            'line-color':'#808000',
            'width':1
        }
    },
    {
        'selector': '.18e',
        'style':{
            'line-color':'#f3e100',
            'width':1
        }
    },
    {
        'selector': '.19e',
        'style':{
            'line-color':'#ffb900',
            'width':1
        }
    },
    {
        'selector': '.20e',
        'style':{
            'line-color':'#dc0000',
            'width':1
        }
    },
    {
        'selector': '.21e',
        'style':{
            'line-color':'#ff3900',
            'width':1
        }
    },
    {
        'selector': '.22e',
        'style':{
            'line-color':'#fe0000',
            'width':1
        }
    },
    {
        'selector': '.23e',
        'style':{
            'line-color':'#cc0c0c',
            'width':1
        }
    },
    {
        'selector': '.24e',
        'style':{
            'line-color':'#00aaa0',
            'width':1
        }
    },
    {
        'selector': '.25e',
        'style':{
            'line-color':'#009dcf',
            'width':1
        }
    },
    {
        'selector': '.26e',
        'style':{
            'line-color':'#00b600',
            'width':1
        }
    },
    {
        'selector': '.27e',
        'style':{
            'line-color':'#120015',
            'width':1
        }
    },
    {
        'selector': '.28e',
        'style':{
            'line-color':'#ffa500',
            'width':1
        }
    },
    {
        'selector': '.29e',
        'style':{
            'line-color':'#70007f',
            'width':1
        }
    },
    {
        'selector': '.30e',
        'style':{
            'line-color':'#00a45d',
            'width':1
        }
    },
    {
        'selector': '.31e',
        'style':{
            'line-color':'#00a900',
            'width':1
        }
    },
    {
        'selector': '.32e',
        'style':{
            'line-color':'#f10000',
            'width':1
        }
    },
    {
        'selector': '.33e',
        'style':{
            'line-color':'#cf0000',
            'width':1
        }
    },
    {
        'selector': '.34e',
        'style':{
            'line-color':'#cbf900',
            'width':1
        }
    },
    {
        'selector': '.35e',
        'style':{
            'line-color':'#009b12',
            'width':1
        }
    },
    {
        'selector': '.36e',
        'style':{
            'line-color':'#ff5d00',
            'width':1
        }
    },
    {
        'selector': '.37e',
        'style':{
            'line-color':'#4d00a0',
            'width':1
        }
    },
    {
        'selector': '.38e',
        'style':{
            'line-color':'#001cdd',
            'width':1
        }
    },
    {
        'selector': '.39e',
        'style':{
            'line-color':'#83ff00',
            'width':1
        }
    },
    {
        'selector': '.40e',
        'style':{
            'line-color':'#1dff00',
            'width':1
        }
    },
    {
        'selector': '.41e',
        'style':{
            'line-color':'#00e700',
            'width':1
        }
    },
    {
        'selector': '.42e',
        'style':{
            'line-color':'#ff2000',
            'width':1
        }
    },
    {
        'selector': '.43e',
        'style':{
            'line-color':'#002edd',
            'width':1
        }
    },
    {
        'selector': '.44e',
        'style':{
            'line-color':'#0000d5',
            'width':1
        }
    },
    {
        'selector': '.45e',
        'style':{
            'line-color':'#009e27',
            'width':1
        }
    },
    {
        'selector': '.46e',
        'style':{
            'line-color':'#009c00',
            'width':1
        }
    },
    {
        'selector': '.47e',
        'style':{
            'line-color':'#008ddd',
            'width':1
        }
    },
    {
        'selector': '.48e',
        'style':{
            'line-color':'#00a247',
            'width':1
        }
    },
    {
        'selector': '.49e',
        'style':{
            'line-color':'#004add',
            'width':1
        }
    },
    {
        'selector': '.50e',
        'style':{
            'line-color':'#f7d900',
            'width':1
        }
    },
    {
        'selector': '.51e',
        'style':{
            'line-color':'#0200a9',
            'width':1
        }
    },
    {
        'selector': '.52e',
        'style':{
            'line-color':'#00aaa8',
            'width':1
        }
    },
    {
        'selector': '.53e',
        'style':{
            'line-color':'#00aa8d',
            'width':1
        }
    },
    {
        'selector': '.54e',
        'style':{
            'line-color':'#3700a3',
            'width':1
        }
    },
    {
        'selector': '.55e',
        'style':{
            'line-color':'#00e100',
            'width':1
        }
    },
    {
        'selector': '.56e',
        'style':{
            'line-color':'#e30000',
            'width':1
        }
    },
    {
        'selector': '.57e',
        'style':{
            'line-color':'#00fc00',
            'width':1
        }
    },
    {
        'selector': '.58e',
        'style':{
            'line-color':'#1700a7',
            'width':1
        }
    },
    {
        'selector': '.59e',
        'style':{
            'line-color':'#3aff00',
            'width':1
        }
    },
    {
        'selector': '.60e',
        'style':{
            'line-color':'#66ff00',
            'width':1
        }
    },
    {
        'selector': '.61e',
        'style':{
            'line-color':'#d7f500',
            'width':1
        }
    },
    {
        'selector': '.62e',
        'style':{
            'line-color':'#870098',
            'width':1
        }
    },
    {
        'selector': '.63e',
        'style':{
            'line-color':'#2e0035',
            'width':1
        }
    },
    {
        'selector': '.64e',
        'style':{
            'line-color':'#0066dd',
            'width':1
        }
    },
    {
        'selector': '.65e',
        'style':{
            'line-color':'#0000b5',
            'width':1
        }
    },
    {
        'selector': '.66e',
        'style':{
            'line-color':'#00d400',
            'width':1
        }
    },
    {
        'selector': '.67e',
        'style':{
            'line-color':'#000000',
            'width':1
        }
    },
    {
        'selector': '.68e',
        'style':{
            'line-color':'#cc2c2c',
            'width':1
        }
    },
    {
        'selector': '.69e',
        'style':{
            'line-color':'#0077dd',
            'width':1
        }
    },
    {
        'selector': '.70e',
        'style':{
            'line-color':'#ff8100',
            'width':1
        }
    },
    {
        'selector': '.71e',
        'style':{
            'line-color':'#0000c9',
            'width':1
        }
    },
    {
        'selector': '.72e',
        'style':{
            'line-color':'#0000bd',
            'width':1
        }
    },
    {
        'selector': '.73e',
        'style':{
            'line-color':'#d90000',
            'width':1
        }
    },
    {
        'selector': '.74e',
        'style':{
            'line-color':'#f1e700',
            'width':1
        }
    },
    {
        'selector': '.75e',
        'style':{
            'line-color':'#0099db',
            'width':1
        }
    },
    {
        'selector': '.76e',
        'style':{
            'line-color':'#00a87d',
            'width':1
        }
    },
    {
        'selector': '.77e',
        'style':{
            'line-color':'#5d006a',
            'width':1
        }
    },
    {
        'selector': '.78e',
        'style':{
            'line-color':'#dff200',
            'width':1
        }
    },
    {
        'selector': '.79e',
        'style':{
            'line-color':'#00be00',
            'width':1
        }
    },
    {
        'selector': '.80e',
        'style':{
            'line-color':'#ebee00',
            'width':1
        }
    },
    {
        'selector': '.81e',
        'style':{
            'line-color':'#7e008e',
            'width':1
        }
    },
    {
        'selector': '.82e',
        'style':{
            'line-color':'#00a7b3',
            'width':1
        }
    },
    {
        'selector': '.83e',
        'style':{
            'line-color':'#00f400',
            'width':1
        }
    },
    {
        'selector': '.84e',
        'style':{
            'line-color':'#cc5c5c',
            'width':1
        }
    },
    {
        'selector': '.85e',
        'style':{
            'line-color':'#00ef00',
            'width':1
        }
    },
    {
        'selector': '.86e',
        'style':{
            'line-color':'#cccccc',
            'width':1
        }
    },
    {
        'selector': '.87e',
        'style':{
            'line-color':'#00aa9a',
            'width':1
        }
    },
    {
        'selector': '.88e',
        'style':{
            'line-color':'#fad400',
            'width':1
        }
    },
    {
        'selector': '.89e',
        'style':{
            'line-color':'#c3fb00',
            'width':1
        }
    },
    {
        'selector': '.90e',
        'style':{
            'line-color':'#cc7c7c',
            'width':1
        }
    },
    {
        'selector': '.91e',
        'style':{
            'line-color':'#d50000',
            'width':1
        }
    },
    {
        'selector': '.92e',
        'style':{
            'line-color':'#0000dd',
            'width':1
        }
    },
    {
        'selector': '.93e',
        'style':{
            'line-color':'#6d009c',
            'width':1
        }
    },
    {
        'selector': '.94e',
        'style':{
            'line-color':'#eb0000',
            'width':1
        }
    },
    {
        'selector': '.95e',
        'style':{
            'line-color':'#d30000',
            'width':1
        }
    },
    {
        'selector': '.96e',
        'style':{
            'line-color':'#00cc00',
            'width':1
        }
    },
    {
        'selector': '.97e',
        'style':{
            'line-color':'#00a4bb',
            'width':1
        }
    },
    {
        'selector': '.98e',
        'style':{
            'line-color':'#fecc00',
            'width':1
        }
    },
    {
        'selector': '.99e',
        'style':{
            'line-color':'#00a100',
            'width':1
        }
    },

]