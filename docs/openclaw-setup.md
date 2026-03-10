# OpenClaw Setup Guide

This guide explains how to run this framework with OpenClaw cron jobs.

## 1) Map manifests to cron jobs
Use files in `jobs/manifests/`:
- `h00`–`h09`: audit lanes
- `h10`–`h19`: PR attempt lanes

Each manifest defines lane type, prompt path, and expected outcomes.

## 2) Use isolated sessions for lane jobs
Recommended:
- `sessionTarget: isolated`
- one lane per job
- explicit timeout per lane

## 3) Keep alerting strict
Only alert for real execution failures:
- command failure
- tool/auth failure
- artifact write failure

Do not alert repeatedly for unresolved backlog items.

## 4) Keep message outputs human-readable
Use templates in `prompts/reporting/` and rules in `contracts/messaging-contract.md`.

## 5) Preserve artifacts
At minimum per lane:
- hourly summary
- status JSON
- run-proof JSON

Validate against `schemas/`.
