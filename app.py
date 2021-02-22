#!/usr/bin/env python3

from aws_cdk import core

from mycdkproject.mycdkproject_stack import MycdkprojectStack


app = core.App()
MycdkprojectStack(app, "mycdkproject")

app.synth()
