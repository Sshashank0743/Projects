package com.bracketcove.graphsudoku.common

import android.app.job.JobInfo

abstract class BaseLogic<EVENT> {
    protected lateinit var jobTracker: Job
    abstract fun onEvent(event: EVENT)
}