class Color(DefaultColor):
    USERNAME_FG = 8
    USERNAME_BG = 251
    USERNAME_ROOT_BG = 209

    HOSTNAME_FG = 8
    HOSTNAME_BG = 7

    HOME_SPECIAL_DISPLAY = True
    HOME_FG = 4
    PATH_BG = 7
    PATH_FG = 14
    SEPARATOR_FG = 14
    CWD_BG = 4
    CWD_FG = 7

    READONLY_BG = 209
    READONLY_FG = 15

    # REPO_CLEAN_BG = 150  # pale green
    REPO_CLEAN_BG = 149  # greener pale green
    REPO_CLEAN_FG = 235
    # REPO_DIRTY_BG = 203  # pale red
    REPO_DIRTY_BG = 178  # pale yellow
    REPO_DIRTY_FG = 15

    GIT_UNTRACKED_BG = 9
    GIT_NOTSTAGED_BG = 0
    GIT_AHEAD_BG = 4
    GIT_AHEAD_FG = DefaultColor.GIT_UNTRACKED_FG

    JOBS_FG = 14
    JOBS_BG = 8

    CMD_PASSED_BG = 7
    CMD_PASSED_FG = 8
    CMD_FAILED_BG = 9
    CMD_FAILED_FG = 15

    SVN_CHANGES_BG = REPO_DIRTY_BG
    SVN_CHANGES_FG = REPO_DIRTY_FG

    VIRTUAL_ENV_BG = 150
    VIRTUAL_ENV_FG = 0
