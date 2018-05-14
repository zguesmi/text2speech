import sys, yaml


class FatalError(Exception):

    def __init__(self, message):
        sys.exit(message)


class ConfigFileNotFoundError(FatalError):

    message = 'Input config file not found - {}'

    def __init__(self, filename):
        super().__init__(self.message.format(filename))


class UnrespectedConfigFormatError(FatalError):

    message = 'Error parsing input config file - required format is name:lang\n{}'

    def __init__(self, err):
        super().__init__(self.message.format(err))


class CustomError(Exception):

    def __init__(self, message):
        print(message)


class FileNotFoundError(CustomError):

    message = 'File not found - {}'

    def __init__(self, filename):
        super().__init__(self.message.format(filename))


class FileTypeNotSupportedError(CustomError):

    message = 'File type not supported - {}'

    def __init__(self, filename):
        super().__init__(self.message.format(filename))


class IllegalVoiceNameError(CustomError):

    message = 'Unsupported voice - "{}"\nDefaulting to "{}"'

    def __init__(self, voice, default):
        super().__init__(self.message.format(voice, default))


class IllegalLatencyError(CustomError):

    message = 'Illegal latency value - "{}"\nLatency should be in [0.0 .. 2.0]. Defaulting to "{}"'

    def __init__(self, latency, default):
        super().__init__(self.message.format(latency, default))


class CanNotConvertTextToSpeechError(CustomError):

    message = 'Error extracting text from image - {}\n{}'

    def __init__(self, err, filename):
        super().__init__(self.message.format(filename, err))


class CanNotCreateConsensusFile(FatalError):

    message = 'Error creating consensus file - {}\n{}'

    def __init__(self, err, filename):
        super().__init__(self.message.format(filename, err))