from pygments.style import Style
from pygments.token import Token, Comment, Keyword, Name, String, \
     Error, Generic, Number, Operator


class main_style(Style):

    styles = {
        Token:                  '',
        Comment:                'italic #c8c8c8',
        Keyword:                'bold #017494',
        Name:                   '#f00',
        Name.Class:             'bold #FE5F55',
        Name.Function:          '#A64942',
        String:                 'bg:#31355a'
    }