# Copyright (c) 2012-2019, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 8.0.0


from . import AWSObject
from . import AWSProperty
from .validators import boolean
from .validators import double


class CostTypes(AWSProperty):
    props = {
        'IncludeCredit': (boolean, False),
        'IncludeDiscount': (boolean, False),
        'IncludeOtherSubscription': (boolean, False),
        'IncludeRecurring': (boolean, False),
        'IncludeRefund': (boolean, False),
        'IncludeSubscription': (boolean, False),
        'IncludeSupport': (boolean, False),
        'IncludeTax': (boolean, False),
        'IncludeUpfront': (boolean, False),
        'UseAmortized': (boolean, False),
        'UseBlended': (boolean, False),
    }


class Spend(AWSProperty):
    props = {
        'Amount': (double, True),
        'Unit': (basestring, True),
    }


class TimePeriod(AWSProperty):
    props = {
        'End': (basestring, False),
        'Start': (basestring, False),
    }


class BudgetData(AWSProperty):
    props = {
        'BudgetLimit': (Spend, False),
        'BudgetName': (basestring, False),
        'BudgetType': (basestring, True),
        'CostFilters': (dict, False),
        'CostTypes': (CostTypes, False),
        'PlannedBudgetLimits': (dict, False),
        'TimePeriod': (TimePeriod, False),
        'TimeUnit': (basestring, True),
    }


class Notification(AWSProperty):
    props = {
        'ComparisonOperator': (basestring, True),
        'NotificationType': (basestring, True),
        'Threshold': (double, True),
        'ThresholdType': (basestring, False),
    }


class Subscriber(AWSProperty):
    props = {
        'Address': (basestring, True),
        'SubscriptionType': (basestring, True),
    }


class NotificationWithSubscribers(AWSProperty):
    props = {
        'Notification': (Notification, True),
        'Subscribers': ([Subscriber], True),
    }


class Budget(AWSObject):
    resource_type = "AWS::Budgets::Budget"

    props = {
        'Budget': (BudgetData, True),
        'NotificationsWithSubscribers':
            ([NotificationWithSubscribers], False),
    }
