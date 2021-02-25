#!/usr/bin/env python3

from aws_cdk import core

from mycdkproject.vpc_stack import VPCStack
from mycdkproject.eks_stack import EKSStack
app = core.App()
vpc_stack = VPCStack(app, "mycdkproject")
eks_stack = EKSStack(app,'eks',vpc=vpc_stack.vpc)
app.synth()
