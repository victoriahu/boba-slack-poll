from slacker import Slacker

slack = Slacker('')


channel_id = slack.channels.get_channel_id('test')
slack.chat.command(
        channel='CGN0GQ9V5',
        command='/boba',
        text='"Do you prefer milk tea or fruit tea?" "Milk" "Fruit"'
)