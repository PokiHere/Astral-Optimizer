import time


chemin_fortnite_settings = "C:\\Users\\estev\\AppData\\Local\\FortniteGame\\Saved\\Config\\WindowsClient\\GameUserSettings.ini"


nouveau_contenu = """
[/Script/FortniteGame.FortGameUserSettings]
CosmeticStreamingEnabled=CodeSet_Enabled
FortniteReleaseVersion=7
UnlockConsoleFPS=False
SubGameSelectCount_Athena=5
SubGameLastSelectedTime_Athena=2023.12.10-18.58.23
SubGameSelectCount_Campaign=0
SubGameLastSelectedTime_Campaign=0001.01.01-00.00.00
LastTimeSettingsSnapshotUploaded=2023.12.10-16.26.18
FirstLoginOnDevice=2023.12.10-17.19.12
SafeZone=1.000000
bIsSafeZoneSet=False
CachedPlayerLevel=0
bShowActorsWithSeasonItemTagMapIndicators=True
CachedBattleStars=0
CachedAlienStylePoints=0
CachedStylePoints=0
CachedClaimableRewards=()
CachedHighestBattlePassUnlockedPage=1
bShowCareerTabBang=False
CustomVoiceChatInputDevice=
CustomVoiceChatOutputDevice=
CustomVoiceChatInputDeviceId=
CustomVoiceChatOutputDeviceId=
bMotionBlur=False
bShowGrass=False
bShowFPS=True
bUseGPUCrashDebugging=False
bStopRenderingInBackground=False
bLatencyTweak1=False
LatencyTweak2=0
bLatencyFlash=False
FortAntiAliasingMethod=TSREpic
bEnableDLSSFrameGeneration=False
TemporalSuperResolutionQuality=Recommended
DLSSQuality=0
bUseNanite=False
DesiredGlobalIlluminationQuality=1
DesiredReflectionQuality=1
PreNaniteGlobalIlluminationQuality=1
PreNaniteReflectionQuality=1
bRayTracing=False
b120FpsMode=False
FrontendFrameRateLimit=120
bIsEnergySavingEnabledIdle=True
bIsEnergySavingEnabledFocusLoss=True
EnergySavingLevelFocusLoss=1
DisplayGamma=1.000000
UserInterfaceContrast=1.000000
NamedTimes=()
NamedCounts=(("EcosystemTrailer", 1),("EcosystemTrailer_HotfixVer", 0),("lastfrontendflow_Fortnite", 28),("lastfrontendflow_Fortnite_HotfixVer", 0),("UEnableMultiFactorModal::ShouldShowMFASplashScreen", 28),("UEnableMultiFactorModal::ShouldShowMFASplashScreen_HotfixVer", 0),("SeasonTrailer", 28),("SeasonTrailer_HotfixVer", 0))
BattlePassOverrideTracker=0
NewestProgressiveCosmeticSetSeen=
CurrentLockerSorts=()
bLockerHideUnsupportedItems=False
bHasUsedBattlePassCrewUpsellNavButton=False
bHasUserSeenQuickSaveTooltip=False
bHasUserSeenLockerActionBarTooltip=False
bHasSeenLockerTemporaryItemsTooltip=False
LastExpectedShopRefreshTime=0001.01.01-00.00.00
bHasSeenItemShop=False
bHasSeenJunoOutfitsFTUE=False
bHasSeenDonutShopSequence=False
DonutIdleGameHighScore=0.000000
DisplayAssetPathToOfferSeenLevel=()
RowIdToOfferSeenLevel=(("HeroAcaAll.Class1-AHeroes.98", Notification))
ItemShopSectionsSeenStateLastResetDates=()
LastSelectedPlaylist=(PlaylistName="Playlist_DefaultSolo",TournamentId="",EventWindowId="",LinkId=(Mnemonic="playlist_defaultsolo",Version=-1),bGracefullyUpgraded=False,MatchmakingRulePreset=RespectParties)
LastSelectedFillOption=True
bLastSelectedPrivateMatchOption=False
CustomMatchOptions=()
CreativeOptions=()
bHasSeenCreativePhoneTutorial=False
bHasSeenCreativeHeatmapTutorial=False
CreativeOptionLastUsedCategory=0
CreativeOptionLastUsedIndexInCategory=0
LastSelectedChildActivityMap=()
LastNewsVersionViewedBR=
LastNewsVersionViewedCreative=
LastNewsVersionViewedSTW=
LastPRMEtag=
LastFrontEndBackPlateStageUsed[0]=defaultnotris
LastFrontEndBackPlateStageUsed[1]=default
bEulaAccepted=True
EulaAcceptedUserId=6ccc97f6bb4f4eef9c85ddf62e69fcd2
LastEulaCheckTime=2023.12.10-16.26.14
HUDLayoutData[0]=(LayoutEntries=)
HUDLayoutData[1]=(LayoutEntries=)
HUDLayoutData[2]=(LayoutEntries=)
ActiveHUDProfileIdentifier=(HUDProfileType=(TagName=""),Guid=00000000000000000000000000000000)
bTimesSeenBacchusLoadTutorial=0
bHasSeenTapToShoot=False
NumTimesSeeingPanningTip=0
FireModeData=(bAutoFireIsEnabled=True,b3DTouchEnabled=False,bTapToShootEnabled=False,bAlwaysShowDedicatedButton=True,FireModeType=Unset)
SimpleMobileStats=(GamesPlayed=0,SecondsPlayed=0,KillCount=0,BestResult=100,LastReviewPromptDay=0001.01.01-00.00.00,CampaignGamesPlayed=0)
AudioOutputDeviceId=
bUseHeadphoneMode=False
InitialBenchmarkState=1
bDisableMouseAcceleration=True
ChosenLoginType=None
SocialImportOptedOutVersion=0
VKImportOptedOutVersion=0
bHasSeenErebusSocialImport=False
bHasSeenFriendImportToast=False
LastSocialImportPromptTime=0001.01.01-00.00.00
bAutoImportFriendEnabled=False
bSeenLetoSellModal=False
SocialImportPromptCountCurrentVersion=0
SocialImportPromptCountAllVersions=0
VKImportPromptCountCurrentVersion=0
VKImportPromptCountAllVersions=0
LastAccountItemWarningTime=0001.01.01-00.00.00
bMultiFactorAuthModalOpOut=False
LastEnableMFAModalPromptTime=0001.01.01-00.00.00
LastVKImportPromptTime=0001.01.01-00.00.00
LastAffiliateToastTime=0001.01.01-00.00.00
FailedInviteMap=()
MobileRecommendationDismissedVersion=0
ShowLiveStreamPictureInPictureInMatchV2=Default
CurrentLivePiPStreamOverrideCounter=0
SelectedFrontEnd=
bNeverShowMobileLink=False
bHasMigratedDownloadSettings=False
bSendAppsFlyerEventOnInstallation=True
bAllowFullGameDownload=False
bAllowCellularDownload=False
LastAutoDownloadHighResTextureReminder=638378279037890000
bAutoLaunchFullGame=False
bAllowDownloadHighResMips=False
ContentQualityLevelSelected=Unset
bAllowLowPowerMode=False
bAllowVideoPlayback=True
MobileFPSMode=Mode_30Fps
MobileQualitySettingsResetDefaultsGUID=
bHasSeenSamsungPressureSensorWarning=False
bNeverDisplaySamsungPressureSensorWarning=False
bHasRecentlySeenBadMatchPopup=False
MatchesSinceLastBadMatchPopup=0
bHasAlreadyRatedOnGooglePlay=False
DaysToSnoozeBeforeNextGooglePlayRating=0
GooglePlayRatingDelayedOccurences=0
bShowTemperature=False
LastGameStartNotificationSentTime=0001.01.01-00.00.00
LastYearForcedDisplayWinterfestInfoButton=0
LastYearWinterfestWasSeen=0
bHasSeenSidekickWelcomePopup=False
bHasSeenLobbyModeSetNotification=False
bHasSeenLobbyModeChangedNotification=False
bHasSeenDiscoveryModeSetNotification=False
bHasSeenDiscoveryCCUModal=False
HasSeenDiscoveryDetailsModeSetNotificationMnemonics=()
bHasSeenCreatorPageFirstTimeTooltip=False
LowInputLatencyModeIsEnabled=True
bNeedsToSeeFireModeSelectionReminder=False
MatchesSinceInitialFireModeSelection=0
bUseVSync=False
bUseDynamicResolution=False
ResolutionSizeX=1920
ResolutionSizeY=1080
LastUserConfirmedResolutionSizeX=1920
LastUserConfirmedResolutionSizeY=1080
WindowPosX=-1
WindowPosY=-1
LastConfirmedFullscreenMode=0
PreferredFullscreenMode=0
AudioQualityLevel=0
LastConfirmedAudioQualityLevel=0
FrameRateLimit=240.000000
DesiredScreenWidth=1280
DesiredScreenHeight=720
LastUserConfirmedDesiredScreenWidth=1280
LastUserConfirmedDesiredScreenHeight=720
LastRecommendedScreenWidth=-1.000000
LastRecommendedScreenHeight=-1.000000
LastCPUBenchmarkResult=-1.000000
LastGPUBenchmarkResult=-1.000000
LastGPUBenchmarkMultiplier=1.000000
bUseHDRDisplayOutput=False
HDRDisplayOutputNits=1000
FullscreenMode=0

[RayTracing]
r.RayTracing.EnableInGame=False

[ScalabilityGroups]
sg.ResolutionQuality=80
sg.ViewDistanceQuality=0
sg.AntiAliasingQuality=0
sg.ShadowQuality=0
sg.GlobalIlluminationQuality=0
sg.ReflectionQuality=0
sg.PostProcessQuality=0
sg.TextureQuality=0
sg.EffectsQuality=0
sg.FoliageQuality=0
sg.ShadingQuality=0
sg.LandscapeQuality=0

[ChatSettings]
HideSocialName=False
AutoImportFriends=False
ShowNotifications=True
NeverFadeMessages=False
ShowTimeStamps=True
ShowWhispersInAllTabs=False
ShowCustomTab=False
ShowWhispersTab=False
ShowGlobalTab=True
ShowCombatAndEventsTab=True
ShowClanTabs=True
HideOffline=False
HideOutgoing=False
HideSuggestions=False
HideRecent=False
HideBlocked=True
FilterMatureLanguage=False
DisplayCharacterNames=False
FriendInviteReceivedCueEnabled=False
GameOrPartyInviteReceivedCueEnabled=False
MessageReceivedCueEnabled=False
SoundEnabled=False
ShowTextChat=True
FontSize=1
WindowHeight=0
WindowOpacity=0.5

[D3DRHIPreference]
PreferredRHI=dx11
PreferredFeatureLevel=es31







"""

with open(chemin_fortnite_settings, 'w') as fichier:
    fichier.write(nouveau_contenu)

print("GameUserSettings has been suscesfully optimised")
time.sleep(2)



