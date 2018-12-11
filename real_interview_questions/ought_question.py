
import string
import random


class Message:
    pointer_prepeding_character = '#'
    pointer_appending_character = '#'

    def get_new_pointer_identifier(self):
        size = 10
        chars=string.ascii_uppercase + string.digits
        return ''.join(random.choice(chars) for _ in range(size))

    def __init__(self, input_text, pointer_to_message=None):
        if pointer_to_message == None:
            pointer_to_message = {}
        self.context = {'pointer_to_message': pointer_to_message, 'pointer_ordering': []}

        self.text = ''
        self.sub_messages = []

        bracket_stack = []
        start_sub_message_index = 0
        for index in range(len(input_text)):
            character = input_text[index]

            if character == '[':
                if len(bracket_stack) == 0:
                    self.text += input_text[start_sub_message_index:index]
                    start_sub_message_index = index
                bracket_stack.append('[')

            if character == ']':
                bracket_stack.pop()

                if len(bracket_stack) == 0:
                    # Want to strip off the brackets so start one higher and end one lower
                    new_pointer_identifier = self.get_new_pointer_identifier()
                    self.context['pointer_ordering'].append(new_pointer_identifier)
                    self.context['pointer_to_message'][new_pointer_identifier] = Message(input_text[start_sub_message_index+1: index])

                    self.text += '{}{}{}'.format(self.pointer_prepeding_character, new_pointer_identifier, self.pointer_appending_character)
                    start_sub_message_index = index + 1


        self.text += input_text[start_sub_message_index:]

    def __str__(self):
        return self.text

    def get_pointer_index(self, pointer_name):
        stripped_string = pointer_name.strip(self.pointer_prepeding_character)

        try:
            pointer_integer = int(stripped_string) - 1
            return pointer_integer
        except:
            print('You tried to pass an invalid pointer')
            raise

    def get_pointed_at_message(self, pointer_name):
            # just storing our pointers in an ordered list
            pointer_key = self.context['pointer_ordering'][self.get_pointer_index(pointer_name)]
            return self.context['pointer_to_message'][pointer_key]

    def map_string_to_external_sting(self, internal_string, pointer_to_display_pointer):
        external_string = ''

        index = 0
        while (index < len(internal_string)):
            if (internal_string[index] == self.pointer_prepeding_character):
                index += 1
                start_index = index
                while(index < len(internal_string) and internal_string[index] != self.pointer_appending_character):
                    index += 1

                pointer = internal_string[start_index: index]
                external_string += pointer_to_display_pointer[pointer]
                index += 1

            else:
                external_string += internal_string[index]
                index += 1

        return external_string

    def get_pointer_to_display_pointer_mapping(self):
        pointer_to_display_pointer = {}

        for i in range(len(self.context['pointer_ordering'])):
            pointer_to_display_pointer[self.context['pointer_ordering'][i]] = '{}{}'.format(self.pointer_prepeding_character, i+1)

        return pointer_to_display_pointer



class Command:
    def __init__(self, message):
        self.message = message
        self.response_message = None
        self.sub_commands = []
        self.operations = []

    def display(self):
        pointer_to_display_pointer = self.message.get_pointer_to_display_pointer_mapping()

        print(self.message.map_string_to_external_sting(self.message.text, pointer_to_display_pointer))

        sub_commands = 0
        for sub_command in self.sub_commands:
            sub_commands += 1

            sub_message = sub_command.message

            print('{}. {}'.format(sub_commands, self.message.map_string_to_external_sting('{} => {}'.format(sub_message, sub_command.response_message), pointer_to_display_pointer)))


class ViewOperation():
    def __init__(self, display_pointer_name):
        self.display_pointer_name = display_pointer_name

    def run(self, command):
        message = command.message
        sub_message = message.get_pointed_at_message(self.display_pointer_name)

        pointer_index = message.get_pointer_index(self.display_pointer_name)
        internal_pointer_name = message.context['pointer_ordering'][pointer_index]

        new_pointers = message.context['pointer_ordering'][:pointer_index] + message.context['pointer_ordering'][pointer_index + 1:]

        new_message_text = message.text.replace('{}{}{}'.format(Message.pointer_prepeding_character, internal_pointer_name, Message.pointer_appending_character), '[{}]'.format(sub_message.text))

        message.text = new_message_text
        message.context['pointer_ordering'] = new_pointers

        del message.context['pointer_to_message'][internal_pointer_name]

        for sub_message_pointer in sub_message.context['pointer_ordering']:
            if sub_message_pointer not in message.context['pointer_to_message']:
                message.context['pointer_to_message'][sub_message_pointer] = sub_message.context['pointer_to_message'][sub_message_pointer]
                message.context['pointer_ordering'].append(sub_message_pointer)

        return command


class AskOperation:
    def __init__(self, ask_text):
        self.ask_text = ask_text

    def _get_message_for_new_ask_command(self, old_message, new_text_command):
        new_string = ''
        pointers = []

        index = 0
        while index < len(new_text_command):
            if new_text_command[index] == Message.pointer_prepeding_character:
                start_index = index
                index += 1

                while index < len(new_text_command) and new_text_command[index] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    index += 1

                pointer_index = old_message.get_pointer_index(new_text_command[start_index: index])
                pointer_name = old_message.context['pointer_ordering'][pointer_index]
                new_string += '{}{}{}'.format(Message.pointer_prepeding_character, pointer_name, Message.pointer_appending_character)
                pointers.append(pointer_name)
            else:
                new_string += new_text_command[index]
                index += 1

        new_message = Message(new_string)
        new_message.context['pointer_ordering'] = pointers
        return new_message

    def run(self, command):
        new_command = Command(self._get_message_for_new_ask_command(command.message, self.ask_text))
        command.sub_commands.append(new_command)
        return new_command



class ReplyOperation:
    def __init__(self, reply_text):
        self.reply_text = reply_text

    def run(self, command):
        command.response_message = Message(self.reply_text)

        for pointer_in_reply in command.response_message.context['pointer_ordering']:
            if pointer_in_reply not in command.message.context['pointer_to_message']:
                command.message.context['pointer_ordering'].append(pointer_in_reply)
                command.message.context['pointer_to_message'][pointer_in_reply] = command.response_message.context['pointer_to_message'][pointer_in_reply]

        return command

def rec_run_command(command, cache):
    already_entered_loop = False

    while True:
        if command.message.text in cache and not already_entered_loop:
            cache_command = cache[command.message.text]
            cache_command.message.context = command.message.context

            for operation in cache_command.operations:
                sub_command = operation.run(cache_command)

            command.message = cache_command.message
            command.response_message = cache_command.response_message
            return
        else:
            cache[command.message.text] = command

        already_entered_loop = True

        command.display()

        response_string = get_terminal_sanitized_input_string()

        if response_string.startswith('ask'):
            new_question = response_string.split('ask ')[1]

            new_operation = AskOperation(new_question)
            command.operations.append(new_operation)
            sub_command = new_operation.run(command)
            rec_run_command(sub_command, cache)

            # copy over pointers that the sub_command uses to this context
            for sub_pointer in sub_command.message.context['pointer_ordering']:
                if sub_pointer not in command.message.context['pointer_to_message']:
                    command.message.context['pointer_ordering'].append(sub_pointer)
                    command.message.context['pointer_to_message'][sub_pointer] = sub_command.message.context['pointer_to_message'][sub_pointer]

            if sub_command.response_message:
                for sub_pointer in sub_command.response_message.context['pointer_ordering']:
                    if sub_pointer not in command.message.context['pointer_to_message']:
                        command.message.context['pointer_ordering'].append(sub_pointer)
                        command.message.context['pointer_to_message'][sub_pointer] = sub_command.response_message.context['pointer_to_message'][sub_pointer]



        elif response_string.startswith('reply'):
            new_answer = response_string.split('reply ')[1]

            new_operation = ReplyOperation(new_answer)
            command.operations.append(new_operation)
            new_operation.run(command)
            return


        elif response_string.startswith('view'):
            pointer_display_name = response_string.split('view ')[1]

            new_operation = ViewOperation(pointer_display_name)
            command.operations.append(new_operation)
            rec_run_command(new_operation.run(command), cache)
            return





def get_terminal_sanitized_input_string():
    terminal_input_string = '> '
    cleared_screen_string = '---'

    input_string = input(terminal_input_string)
    print(input_string)
    return_string = sanitize_input_string(input_string)
    print(cleared_screen_string)
    return return_string


def sanitize_input_string(string):
    return string

def terminal_application():
    statement_to_actions_cache = {}

    while True:
        print('What is your question?')
        top_level_question = get_terminal_sanitized_input_string()
        command = Command(Message(top_level_question))

        rec_run_command(command, statement_to_actions_cache)

        pointer_to_display_pointer = command.message.get_pointer_to_display_pointer_mapping()
        print(command.message.map_string_to_external_sting('{} => {}'.format(command.message, command.response_message), pointer_to_display_pointer))
        print()

def main():
    terminal_application()


if __name__ == '__main__':
    main()
























# from copy import deepcopy

# class AnswerTreeNode:
#     def __init__(self, sub_nodes, pointers):
#         self.sub_nodes = sub_nodes
#         self.pointers = pointers

# class QuestionNode(AnswerTreeNode):
#     def __init__(self, question, answer, sub_nodes, pointers):
#         AnswerTreeNode.__init__(sub_nodes, pointers)
#         self.question = question
#         self.answer = None

#     def __str__(self):
#         return '{} => {}'.format(self.question, self.answer)

# class ViewNode(AnswerTreeNode):
#     def __init__(self, command, sub_nodes, pointers):
#         AnswerTreeNode.__init__(sub_nodes, pointers)
#         self.command = command

#     def __str__(self):
#         return '{}'.format(self.command)



# def get_duplicate_node_with_new_context(node, new_context):
#     new_node = QuestionTreeNode(node.question, node.answer, node.sub_nodes)
#     new_node.context = deepcopy(new_context)
#     return new_node

# def format_question_answer_string(node):
#     return '{} => {}'.format(node.question, node.answer)

# def display_node(node):
#     print(node.question)

#     sub_node_count = 1
#     for sub_node in node.sub_nodes:
#         print('{}. {}'.format(sub_node_count, format_question_answer_string(sub_node)))
#         sub_node_count += 1

# def evaluate_actions_from_cache_on_node(node, cache):

#     # should I just return the original node back here?
#     return node



# def recursive_terminal_response(node, cache):
#     while True:
#         # what do I need to do with the evaluated actions from the node
#         if node.question in cache:
#             return recursive_terminal_response(get_duplicate_node_with_new_context(cache[node.question], node.context))

#         display_node(node)

#         response_string = get_terminal_sanitized_input_string()

#         if response_string.startswith('ask'):
#             new_question = response_string.split('ask ')[1]
#             new_node = QuestionTreeNode(new_question, None, [])
#             node.sub_nodes.append(new_node)

#             recursive_terminal_response(new_node, cache)

#         elif response_string.startswith('reply'):
#             new_answer = response_string.split('reply ')[1]
#             node.answer = new_answer

#             cache[node.question] = node.answer
#             return

#         elif response_string.startswith('view'):

#             pointer_name = response_string.split('view ')[1]
#             node.sub_nodes

#             cache[node.question] =

#         else:
#             raise Exception('Not valid terminal input')



# def get_message_for_new_command(old_message, new_text_command):
#     pointers = []
#     text = ''
#     old_to_new_pointer_name = {}

#     pointers_seen = 0
#     index = 0
#     while index < len(new_text_command):

#         if new_text_command[index] == Message.pointer_prepeding_character:
#             # move to the right one to start tracking the number
#             index += 1

#             start_index = index
#             while index < len(new_text_command) and new_text_command[index] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
#                 index += 1

#             old_pointer_name = '{}{}'.format(Message.pointer_prepeding_character, new_text_command[start_index: index])
#             if old_pointer_name not in old_to_new_pointer_name:
#                 pointers_seen += 1
#                 old_to_new_pointer_name[old_pointer_name] = '{}{}'.format(Message.pointer_prepeding_character, pointers_seen)
#                 pointers.append(old_message.get_pointed_at_message(old_pointer_name))

#             text += old_to_new_pointer_name[old_pointer_name]
#             index += 1

#         else:
#             text += new_text_command[index]
#             index += 1

#     return Message(text, pointers)

# def get_text_as_response(message, text_response):
#     pointers = []
#     text = ''
#     old_to_new_pointer_name = {}

#     pointers_seen = 0
#     index = 0
#     while index < len(text_response):

#         if text_response[index] == Message.pointer_prepeding_character:
#             # move to the right one to start tracking the number
#             index += 1

#             start_index = index
#             while index < len(text_response) and text_response[index] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
#                 index += 1

#             old_pointer_name = '{}{}'.format(Message.pointer_prepeding_character, text_response[start_index: index])
#             if old_pointer_name not in old_to_new_pointer_name:
#                 pointers_seen += 1
#                 old_to_new_pointer_name[old_pointer_name] = '{}{}'.format(Message.pointer_prepeding_character, pointers_seen)
#                 pointers.append(message.get_pointed_at_message(old_pointer_name))

#             text += old_to_new_pointer_name[old_pointer_name]

#         text += text_response[index]
#         index += 1

#     return Message(text, pointers)
