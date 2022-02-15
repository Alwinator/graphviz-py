import importlib.metadata


class Project:
    @classmethod
    def name(cls):
        return __package__ or __name__

    @classmethod
    def version(cls):
        try:
            return importlib.metadata.version(cls.name())
        except importlib.metadata.PackageNotFoundError:
            return 'dev'
