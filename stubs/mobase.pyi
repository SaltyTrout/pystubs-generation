from enum import Enum
from typing import Dict, Iterable, Iterator, List, Tuple, Union, Any, Optional, Callable, overload
import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtWidgets

class InterfaceNotImplemented: pass

class GuessQuality(Enum):
    INVALID = 0
    FALLBACK = 1
    GOOD = 2
    META = 3
    PRESET = 4
    USER = 5


class InstallResult(Enum):
    SUCCESS = 0
    FAILED = 1
    CANCELED = 2
    MANUAL_REQUESTED = 3
    NOT_ATTEMPTED = 4


class LoadOrderMechanism(Enum):
    FileTime = 0
    PluginsTxt = 1


class ModState(Enum):
    exists = 1
    active = 2
    essential = 4
    empty = 8
    endorsed = 16
    valid = 32
    alternate = 64


class PluginState(Enum):
    missing = 0
    inactive = 1
    active = 2


class ProfileSetting(Enum):
    mods = 1
    configuration = 2
    savegames = 4
    preferDefaults = 8


class ReleaseType(Enum):
    prealpha = 0
    alpha = 1
    beta = 2
    candidate = 3
    final = 4


class SortMechanism(Enum):
    NONE = 0
    MLOX = 1
    BOSS = 2
    LOOT = 3


class VersionScheme(Enum):
    discover = 0
    regular = 1
    decimalmark = 2
    numbersandletters = 3
    date = 4
    literal = 5


class BSAInvalidation:
    def __init__(self): pass
    def activate(self, arg1: "IProfile"): pass
    def deactivate(self, arg1: "IProfile"): pass
    def isInvalidationBSA(self, arg1: str) -> bool: pass


class DataArchives:
    def __init__(self): pass
    def addArchive(self, arg1: "IProfile", arg2: int, arg3: str): pass
    def archives(self, arg1: "IProfile") -> List[str]: pass
    def removeArchive(self, arg1: "IProfile", arg2: str): pass
    def vanillaArchives(self) -> List[str]: pass


class ExecutableInfo:
    def __init__(self, arg1: str, arg2: PyQt5.QtCore.QFileInfo): pass
    def arguments(self) -> List[str]: pass
    def asCustom(self) -> "ExecutableInfo": pass
    def binary(self) -> PyQt5.QtCore.QFileInfo: pass
    def isCustom(self) -> bool: pass
    def isValid(self) -> bool: pass
    def steamAppID(self) -> str: pass
    def title(self) -> str: pass
    def withArgument(self, arg1: str) -> "ExecutableInfo": pass
    def withSteamAppId(self, arg1: str) -> "ExecutableInfo": pass
    def withWorkingDirectory(self, arg1: PyQt5.QtCore.QDir) -> "ExecutableInfo": pass
    def workingDirectory(self) -> PyQt5.QtCore.QDir: pass


class FileInfo:
    @property
    def archive(self) -> str: pass
    @archive.setter
    def archive(self, arg0: str): pass

    @property
    def filePath(self) -> str: pass
    @filePath.setter
    def filePath(self, arg0: str): pass

    @property
    def origins(self) -> List[str]: pass
    @origins.setter
    def origins(self, arg0: List[str]): pass

    def __init__(self): pass


class FileTreeEntry:
    class FileTypes(Enum):
        DIRECTORY = 1
        FILE = 2
        FILE_OR_DIRECTORY = 3

    DIRECTORY = 1
    FILE = 2
    FILE_OR_DIRECTORY = 3

    @overload
    def __eq__(self, arg1: str) -> bool: pass
    @overload
    def __eq__(self, arg1: "FileTreeEntry") -> bool: pass
    @overload
    def __eq__(self, arg1: object) -> bool: pass
    def __repr__(self) -> str: pass
    def detach(self) -> bool: pass
    def fileType(self) -> FileTreeEntry.FileTypes: pass
    def isDir(self) -> bool: pass
    def isFile(self) -> bool: pass
    def moveTo(self, arg1: "IFileTree") -> bool: pass
    def name(self) -> str: pass
    def parent(self) -> Optional[IFileTree]: pass
    def path(self, arg1: str = '\\') -> str: pass
    def pathFrom(self, arg1: "IFileTree", arg2: str = '\\') -> str: pass
    def setTime(self, arg1: PyQt5.QtCore.QDateTime): pass
    def suffix(self) -> str: pass
    def time(self) -> PyQt5.QtCore.QDateTime: pass


class GamePlugins:
    def __init__(self): pass
    def getLoadOrder(self, arg1: List[str]): pass
    def lightPluginsAreSupported(self) -> bool: pass
    def readPluginLists(self, arg1: "IPluginList"): pass
    def writePluginLists(self, arg1: "IPluginList"): pass


class GuessedString:
    @overload
    def __init__(self): pass
    @overload
    def __init__(self, arg1: str, arg2: "GuessQuality"): pass
    def __str__(self) -> str: pass
    @overload
    def reset(self) -> "GuessedString": pass
    @overload
    def reset(self, arg1: str, arg2: "GuessQuality") -> "GuessedString": pass
    @overload
    def reset(self, arg1: "GuessedString") -> "GuessedString": pass
    def setFilter(self, arg1: Callable[[str], Union[str, bool]]): pass
    @overload
    def update(self, arg1: str) -> "GuessedString": pass
    @overload
    def update(self, arg1: str, arg2: "GuessQuality") -> "GuessedString": pass
    def variants(self) -> List[str]: pass


class IDownloadManager:
    def __init__(self): pass
    def downloadPath(self, arg1: int) -> str: pass
    def startDownloadNexusFile(self, arg1: int, arg2: int) -> int: pass
    def startDownloadURLs(self, arg1: List[str]) -> int: pass


class IFileTree(FileTreeEntry):
    class InsertPolicy(Enum):
        FAIL_IF_EXISTS = 0
        REPLACE = 1
        MERGE = 2

    FAIL_IF_EXISTS = 0
    MERGE = 2
    REPLACE = 1

    def __bool__(self) -> bool: pass
    def __getitem__(self, arg1: int) -> "FileTreeEntry": pass
    def __iter__(self) -> Iterator[FileTreeEntry]: pass
    def __len__(self) -> int: pass
    def __repr__(self) -> str: pass
    def addDirectory(self, arg1: str) -> Optional[IFileTree]: pass
    def addFile(self, arg1: str, arg2: PyQt5.QtCore.QDateTime = PyQt5.QtCore.QDateTime()) -> Optional[FileTreeEntry]: pass
    def clear(self) -> bool: pass
    def createOrphanTree(self, arg1: str = '') -> "IFileTree": pass
    def exists(self, arg1: str, arg2: FileTreeEntry.FileTypes = FileTreeEntry.FileTypes.FILE_OR_DIRECTORY) -> bool: pass
    def find(self, arg1: str, arg2: FileTreeEntry.FileTypes = FileTreeEntry.FileTypes.FILE_OR_DIRECTORY) -> Optional[FileTreeEntry]: pass
    def insert(self, arg1: "FileTreeEntry", arg2: IFileTree.InsertPolicy = IFileTree.InsertPolicy.FAIL_IF_EXISTS) -> bool: pass
    def merge(self, arg1: "IFileTree", arg2: bool = False) -> Union[Dict["FileTreeEntry", "FileTreeEntry"], int, bool]: pass
    def move(self, arg1: "FileTreeEntry", arg2: str, arg3: IFileTree.InsertPolicy = IFileTree.InsertPolicy.FAIL_IF_EXISTS) -> bool: pass
    def pathTo(self, arg1: "FileTreeEntry", arg2: str = '\\') -> str: pass
    @overload
    def remove(self, arg1: str) -> bool: pass
    @overload
    def remove(self, arg1: "FileTreeEntry") -> bool: pass
    def removeAll(self, arg1: List[str]) -> int: pass
    def removeIf(self, arg1: Callable[["FileTreeEntry"], bool]) -> int: pass


class IInstallationManager:
    def extractFile(self, arg1: "FileTreeEntry") -> str: pass
    def extractFiles(self, arg1: List["FileTreeEntry"]) -> List[str]: pass
    def installArchive(self, arg1: "GuessedString", arg2: str, arg3: int) -> "InstallResult": pass
    def setURL(self, arg1: str): pass


class IModInterface:
    def __init__(self): pass
    def absolutePath(self) -> str: pass
    def addCategory(self, arg1: str): pass
    def addNexusCategory(self, arg1: int): pass
    def categories(self) -> List[str]: pass
    def name(self) -> str: pass
    def remove(self) -> bool: pass
    def removeCategory(self, arg1: str) -> bool: pass
    def setGamePlugin(self, arg1: "IPluginGame"): pass
    def setIsEndorsed(self, arg1: bool): pass
    def setName(self, arg1: str) -> bool: pass
    def setNewestVersion(self, arg1: VersionInfo): pass
    def setNexusID(self, arg1: int): pass
    def setVersion(self, arg1: VersionInfo): pass


class IModList:
    def __init__(self): pass
    def allMods(self) -> List[str]: pass
    def displayName(self, arg1: str) -> str: pass
    def onModMoved(self, arg1: Callable[[str, int, int], None]) -> bool: pass
    def onModStateChanged(self, arg1: Callable[[str, int], None]) -> bool: pass
    def priority(self, arg1: str) -> int: pass
    def setActive(self, arg1: str, arg2: bool) -> bool: pass
    def setPriority(self, arg1: str, arg2: int) -> bool: pass
    def state(self, arg1: str) -> int: pass


class IModRepositoryBridge:
    def __init__(self): pass
    def requestDescription(self, arg1: str, arg2: int, arg3: PyQt5.QtCore.QVariant): pass
    def requestDownloadURL(self, arg1: str, arg2: int, arg3: int, arg4: PyQt5.QtCore.QVariant): pass
    def requestFileInfo(self, arg1: str, arg2: int, arg3: int, arg4: PyQt5.QtCore.QVariant): pass
    def requestFiles(self, arg1: str, arg2: int, arg3: PyQt5.QtCore.QVariant): pass
    def requestToggleEndorsement(self, arg1: str, arg2: int, arg3: str, arg4: bool, arg5: PyQt5.QtCore.QVariant): pass


class IOrganizer:
    def appVersion(self) -> VersionInfo: pass
    def basePath(self) -> str: pass
    def createMod(self, arg1: "GuessedString") -> "IModInterface": pass
    def createNexusBridge(self) -> "IModRepositoryBridge": pass
    def downloadManager(self) -> "IDownloadManager": pass
    def downloadsPath(self) -> str: pass
    def findFileInfos(self, arg1: str, arg2: Callable[["FileInfo"], bool]) -> List["FileInfo"]: pass
    def findFiles(self, arg1: str, arg2: Callable[[str], bool]) -> List[str]: pass
    def getFileOrigins(self, arg1: str) -> List[str]: pass
    def getGame(self, arg1: str) -> "IPluginGame": pass
    def getMod(self, arg1: str) -> "IModInterface": pass
    def installMod(self, arg1: str, arg2: str = '') -> "IModInterface": pass
    def listDirectories(self, arg1: str) -> List[str]: pass
    def managedGame(self) -> "IPluginGame": pass
    def modDataChanged(self, arg1: "IModInterface"): pass
    def modList(self) -> "IModList": pass
    def modsPath(self) -> str: pass
    def modsSortedByProfilePriority(self) -> List[str]: pass
    def onAboutToRun(self, arg1: Callable[[str], bool]) -> bool: pass
    def onFinishedRun(self, arg1: Callable[[str, int], None]) -> bool: pass
    def onModInstalled(self, arg1: Callable[[str], None]) -> bool: pass
    def overwritePath(self) -> str: pass
    def persistent(self, arg1: str, arg2: str, arg3: PyQt5.QtCore.QVariant = None) -> PyQt5.QtCore.QVariant: pass
    def pluginDataPath(self) -> str: pass
    def pluginList(self) -> "IPluginList": pass
    def pluginSetting(self, arg1: str, arg2: str) -> PyQt5.QtCore.QVariant: pass
    def profile(self) -> "IProfile": pass
    def profileName(self) -> str: pass
    def profilePath(self) -> str: pass
    def refreshModList(self, arg1: bool = True): pass
    def removeMod(self, arg1: "IModInterface") -> bool: pass
    def resolvePath(self, arg1: str) -> str: pass
    def setPersistent(self, arg1: str, arg2: str, arg3: PyQt5.QtCore.QVariant, arg4: bool = True): pass
    def setPluginSetting(self, arg1: str, arg2: str, arg3: PyQt5.QtCore.QVariant): pass
    def startApplication(self, arg1: str, arg2: List[str] = [], arg3: str = '', arg4: str = '', arg5: str = '', arg6: bool = False) -> int: pass
    def waitForApplication(self, arg1: int) -> Tuple[bool, int]: pass


class IPlugin:
    def __init__(self): pass
    def author(self) -> str: pass
    def description(self) -> str: pass
    def init(self, arg1: "IOrganizer") -> bool: pass
    def isActive(self) -> bool: pass
    def name(self) -> str: pass
    def settings(self) -> List["PluginSetting"]: pass
    def version(self) -> VersionInfo: pass


class IPluginDiagnose(IPlugin):
    def __init__(self): pass
    def _invalidate(self): pass
    def activeProblems(self) -> List[int]: pass
    def fullDescription(self, arg1: int) -> str: pass
    def hasGuidedFix(self, arg1: int) -> bool: pass
    def shortDescription(self, arg1: int) -> str: pass
    def startGuidedFix(self, arg1: int): pass


class IPluginFileMapper(IPlugin):
    def __init__(self): pass
    def mappings(self) -> List["Mapping"]: pass


class IPluginGame(IPlugin):
    def __init__(self): pass
    def CCPlugins(self) -> List[str]: pass
    def DLCPlugins(self) -> List[str]: pass
    def binaryName(self) -> str: pass
    def dataDirectory(self) -> PyQt5.QtCore.QDir: pass
    def documentsDirectory(self) -> PyQt5.QtCore.QDir: pass
    def executables(self) -> List["ExecutableInfo"]: pass
    def featureList(self) -> dict: pass
    def gameDirectory(self) -> PyQt5.QtCore.QDir: pass
    def gameIcon(self) -> PyQt5.QtGui.QIcon: pass
    def gameName(self) -> str: pass
    def gameNexusName(self) -> str: pass
    def gameShortName(self) -> str: pass
    def gameVariants(self) -> List[str]: pass
    def gameVersion(self) -> str: pass
    def getLauncherName(self) -> str: pass
    def iniFiles(self) -> List[str]: pass
    def initializeProfile(self, arg1: PyQt5.QtCore.QDir, arg2: int): pass
    def isInstalled(self) -> bool: pass
    def loadOrderMechanism(self) -> "LoadOrderMechanism": pass
    def looksValid(self, arg1: PyQt5.QtCore.QDir) -> bool: pass
    def nexusGameID(self) -> int: pass
    def nexusModOrganizerID(self) -> int: pass
    def primaryPlugins(self) -> List[str]: pass
    def primarySources(self) -> List[str]: pass
    def savegameExtension(self) -> str: pass
    def savegameSEExtension(self) -> str: pass
    def savesDirectory(self) -> PyQt5.QtCore.QDir: pass
    def setGamePath(self, arg1: str): pass
    def setGameVariant(self, arg1: str): pass
    def sortMechanism(self) -> "SortMechanism": pass
    def steamAPPId(self) -> str: pass
    def validShortNames(self) -> List[str]: pass


class IPluginInstaller(IPlugin):
    def isArchiveSupported(self, arg1: "IFileTree") -> bool: pass
    def isManualInstaller(self) -> bool: pass
    def priority(self) -> int: pass
    def setInstallationManager(self, arg1: "IInstallationManager"): pass
    def setParentWidget(self, arg1: PyQt5.QtWidgets.QWidget): pass


class IPluginInstallerCustom:
    def __init__(self): pass
    def _manager(self) -> "IInstallationManager": pass
    def _parentWidget(self) -> PyQt5.QtWidgets.QWidget: pass
    def install(self, arg1: "GuessedString", arg2: str, arg3: str, arg4: str, arg5: int) -> "InstallResult": pass
    @overload
    def isArchiveSupported(self, arg1: "IFileTree") -> bool: pass
    @overload
    def isArchiveSupported(self, arg1: str) -> bool: pass
    def supportedExtensions(self) -> List[str]: pass


class IPluginInstallerSimple(IPluginInstaller):
    def __init__(self): pass
    def _manager(self) -> "IInstallationManager": pass
    def _parentWidget(self) -> PyQt5.QtWidgets.QWidget: pass
    def install(self, arg1: "GuessedString", arg2: "IFileTree", arg3: str, arg4: int) -> Union["InstallResult", "IFileTree", Tuple["InstallResult", "IFileTree", str, int]]: pass


class IPluginList:
    def __init__(self): pass
    def isMaster(self, arg1: str) -> bool: pass
    def loadOrder(self, arg1: str) -> int: pass
    def masters(self, arg1: str) -> List[str]: pass
    def onPluginMoved(self, arg1: Callable[[str, int, int], None]) -> bool: pass
    def onRefreshed(self, arg1: Callable[[None], None]) -> bool: pass
    def origin(self, arg1: str) -> str: pass
    def pluginNames(self) -> List[str]: pass
    def priority(self, arg1: str) -> int: pass
    def setLoadOrder(self, arg1: List[str]): pass
    def setState(self, arg1: str, arg2: int): pass
    def state(self, arg1: str) -> int: pass


class IPluginModPage:
    def __init__(self): pass
    def _parentWidget(self) -> PyQt5.QtWidgets.QWidget: pass
    def displayName(self) -> str: pass
    def handlesDownload(self, arg1: PyQt5.QtCore.QUrl, arg2: PyQt5.QtCore.QUrl, arg3: ModRepositoryFileInfo) -> bool: pass
    def icon(self) -> PyQt5.QtGui.QIcon: pass
    def pageURL(self) -> PyQt5.QtCore.QUrl: pass
    def setParentWidget(self, arg1: PyQt5.QtWidgets.QWidget): pass
    def useIntegratedBrowser(self) -> bool: pass


class IPluginPreview(IPlugin):
    def __init__(self): pass
    def genFilePreview(self, arg1: str, arg2: PyQt5.QtCore.QSize) -> PyQt5.QtWidgets.QWidget: pass
    def supportedExtensions(self) -> List[str]: pass


class IPluginTool(IPlugin):
    def __init__(self): pass
    def _parentWidget(self) -> PyQt5.QtWidgets.QWidget: pass
    def displayName(self) -> str: pass
    def icon(self) -> PyQt5.QtGui.QIcon: pass
    def setParentWidget(self, arg1: PyQt5.QtWidgets.QWidget): pass
    def tooltip(self) -> str: pass


class IProfile:
    def __init__(self): pass
    def absolutePath(self) -> str: pass
    def invalidationActive(self, arg1: InterfaceNotImplemented) -> bool: pass
    def localSavesEnabled(self) -> bool: pass
    def localSettingsEnabled(self) -> bool: pass
    def name(self) -> str: pass


class ISaveGame:
    def __init__(self): pass
    def allFiles(self) -> List[str]: pass
    def getCreationTime(self) -> PyQt5.QtCore.QDateTime: pass
    def getFilename(self) -> str: pass
    def getSaveGroupIdentifier(self) -> str: pass
    def hasScriptExtenderFile(self) -> bool: pass


class ISaveGameInfoWidget(PyQt5.QtWidgets.QWidget):
    def __init__(self, arg1: PyQt5.QtWidgets.QWidget = None): pass
    def setSave(self, arg1: str): pass


class LocalSavegames:
    def __init__(self): pass
    def mappings(self, arg1: PyQt5.QtCore.QDir) -> List["Mapping"]: pass
    def prepareProfile(self, arg1: "IProfile") -> bool: pass


class Mapping:
    @property
    def createTarget(self) -> bool: pass
    @createTarget.setter
    def createTarget(self, arg0: bool): pass

    @property
    def destination(self) -> str: pass
    @destination.setter
    def destination(self, arg0: str): pass

    @property
    def isDirectory(self) -> bool: pass
    @isDirectory.setter
    def isDirectory(self, arg0: bool): pass

    @property
    def source(self) -> str: pass
    @source.setter
    def source(self, arg0: str): pass

    def __init__(self): pass


class ModRepositoryBridge:
    @overload
    def __init__(self): pass
    @overload
    def __init__(self, arg1: "IModRepositoryBridge"): pass
    def onDescriptionAvailable(self, arg1: object): pass
    def onEndorsementToggled(self, arg1: object): pass
    def onFileInfoAvailable(self, arg1: object): pass
    def onFilesAvailable(self, arg1: object): pass
    def onRequestFailed(self, arg1: object): pass
    def requestDescription(self, arg1: str, arg2: int, arg3: PyQt5.QtCore.QVariant): pass
    def requestFileInfo(self, arg1: str, arg2: int, arg3: int, arg4: PyQt5.QtCore.QVariant): pass
    def requestFiles(self, arg1: str, arg2: int, arg3: PyQt5.QtCore.QVariant): pass
    def requestToggleEndorsement(self, arg1: str, arg2: int, arg3: str, arg4: bool, arg5: PyQt5.QtCore.QVariant): pass


class ModRepositoryFileInfo:
    @property
    def categoryID(self) -> int: pass
    @categoryID.setter
    def categoryID(self, arg0: int): pass

    @property
    def description(self) -> str: pass
    @description.setter
    def description(self, arg0: str): pass

    @property
    def fileCategory(self) -> int: pass
    @fileCategory.setter
    def fileCategory(self, arg0: int): pass

    @property
    def fileID(self) -> int: pass
    @fileID.setter
    def fileID(self, arg0: int): pass

    @property
    def fileName(self) -> str: pass
    @fileName.setter
    def fileName(self, arg0: str): pass

    @property
    def fileSize(self) -> int: pass
    @fileSize.setter
    def fileSize(self, arg0: int): pass

    @property
    def fileTime(self) -> PyQt5.QtCore.QDateTime: pass
    @fileTime.setter
    def fileTime(self, arg0: PyQt5.QtCore.QDateTime): pass

    @property
    def gameName(self) -> str: pass
    @gameName.setter
    def gameName(self, arg0: str): pass

    @property
    def modID(self) -> int: pass
    @modID.setter
    def modID(self, arg0: int): pass

    @property
    def modName(self) -> str: pass
    @modName.setter
    def modName(self, arg0: str): pass

    @property
    def name(self) -> str: pass
    @name.setter
    def name(self, arg0: str): pass

    @property
    def newestVersion(self) -> VersionInfo: pass
    @newestVersion.setter
    def newestVersion(self, arg0: VersionInfo): pass

    @property
    def repository(self) -> str: pass
    @repository.setter
    def repository(self, arg0: str): pass

    @property
    def uri(self) -> str: pass
    @uri.setter
    def uri(self, arg0: str): pass

    @property
    def userData(self) -> PyQt5.QtCore.QVariant: pass
    @userData.setter
    def userData(self, arg0: PyQt5.QtCore.QVariant): pass

    @property
    def version(self) -> VersionInfo: pass
    @version.setter
    def version(self, arg0: VersionInfo): pass

    @overload
    def __init__(self): pass
    @overload
    def __init__(self, arg1: "ModRepositoryFileInfo"): pass
    @overload
    def __init__(self, arg1: str = None, arg2: int = None, arg3: int = None): pass
    def __str__(self) -> str: pass
    @staticmethod
    def createFromJson(arg0: str) -> "ModRepositoryFileInfo": pass


class PluginSetting:
    def __init__(self, arg1: str, arg2: str, arg3: PyQt5.QtCore.QVariant): pass


class SaveGameInfo:
    def __init__(self): pass
    def getMissingAssets(self, arg1: str) -> Dict[str, List[str]]: pass
    def getSaveGameInfo(self, arg1: str) -> "ISaveGame": pass
    def getSaveGameWidget(self, arg1: PyQt5.QtWidgets.QWidget) -> Optional[ISaveGameInfoWidget]: pass
    def hasScriptExtenderSave(self, arg1: str) -> bool: pass


class ScriptExtender:
    def __init__(self): pass
    def BinaryName(self) -> str: pass
    def PluginPath(self) -> str: pass
    def getArch(self) -> int: pass
    def getExtenderVersion(self) -> str: pass
    def isInstalled(self) -> bool: pass
    def loaderName(self) -> str: pass
    def loaderPath(self) -> str: pass
    def saveGameAttachmentExtensions(self) -> List[str]: pass


class UnmanagedMods:
    def __init__(self): pass
    def displayName(self, arg1: str) -> str: pass
    def mods(self, arg1: bool) -> List[str]: pass
    def referenceFile(self, arg1: str) -> PyQt5.QtCore.QFileInfo: pass
    def secondaryFiles(self, arg1: str) -> List[str]: pass


class VersionInfo:
    @overload
    def __init__(self): pass
    @overload
    def __init__(self, arg1: str): pass
    @overload
    def __init__(self, arg1: str, arg2: "VersionScheme"): pass
    @overload
    def __init__(self, arg1: int, arg2: int, arg3: int): pass
    @overload
    def __init__(self, arg1: int, arg2: int, arg3: int, arg4: "ReleaseType"): pass
    @overload
    def __init__(self, arg1: int, arg2: int, arg3: int, arg4: int): pass
    @overload
    def __init__(self, arg1: int, arg2: int, arg3: int, arg4: int, arg5: "ReleaseType"): pass
    @overload
    def __eq__(self, arg1: "VersionInfo") -> bool: pass
    @overload
    def __eq__(self, arg1: object) -> bool: pass
    def __ge__(self, arg1: "VersionInfo") -> bool: pass
    def __gt__(self, arg1: "VersionInfo") -> bool: pass
    def __le__(self, arg1: "VersionInfo") -> bool: pass
    def __lt__(self, arg1: "VersionInfo") -> bool: pass
    @overload
    def __ne__(self, arg1: "VersionInfo") -> bool: pass
    @overload
    def __ne__(self, arg1: object) -> bool: pass
    def __str__(self) -> str: pass
    def canonicalString(self) -> str: pass
    def clear(self): pass
    def displayString(self, arg1: int) -> str: pass
    def isValid(self) -> bool: pass
    def parse(self, arg1: str, arg2: "VersionScheme", arg3: bool): pass
    def scheme(self) -> "VersionScheme": pass

