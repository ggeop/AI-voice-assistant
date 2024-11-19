# MIT License

# Copyright (c) 2019 Georgios Papachristou

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import server


class AssistantSkill:
    """
    This class is the parent of all skill classes.
    """

    first_activation = True

    @classmethod
    def console(cls, text='', debug_log=None, info_log=None, warn_log=None, error_log=None, refresh_console=True):
        """
        Prints the text only in console and update the console info.
        """

        cls.console_manager.console_output(text=text,
                                           debug_log=debug_log,
                                           info_log=info_log,
                                           warn_log=warn_log,
                                           error_log=error_log,
                                           refresh_console=refresh_console)

    @classmethod
    def response(cls, text, refresh_console=True):
        """
        The mode of the response depends on the output engine:
            - TTT Engine: The response is only in text
            - TTS Engine: The response is in voice and text
        """
        print(text, refresh_console)

    @classmethod
    def user_input(cls):
        user_input = "voice"
        return user_input

    @classmethod
    def extract_tags(cls, voice_transcript, tags):
        """
        This method identifies the tags from the user transcript for a specific skill.

        e.x
        Let's that the user says "hi jarvis!".
        The skill analyzer will match it with enable_assistant skill which has tags 'hi, hello ..'
        This method will identify the that the enabled word was the 'hi' not the hello.

        :param voice_transcript: string
        :param tags: string
        :return: set
        """

        try:
            transcript_words = voice_transcript.split()
            tags = tags.split(',')
            return set(transcript_words).intersection(tags)
        except Exception as e:
            cls.console_manager.console_output(info_log='Failed to extract tags with message: {0}'.format(e))
            return set()
