"""
mixcoatl.admin.user
-------------------

Implements access to the enStratus User API
"""
from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property

class User(Resource):
    """A user within the enStratus environment"""

    PATH = 'admin/User'
    COLLECTION_NAME = 'users'
    PRIMARY_KEY = 'user_id'

    def __init__(self, user_id=None, *args, **kwargs):
        Resource.__init__(self)
        self.__user_id = user_id

    @property
    def user_id(self):
        """`int` The enStratus unique id of this user across all customer accounts"""
        return self.__user_id

    @lazy_property
    def account(self):
        """`dict` The enStratus account"""
        return self.__account

    @lazy_property
    def account_user_id(self):
        """`str` or `None` A unique identifier to reference this user's access
            to a specific account
        """
        return self.__account_user_id

    @lazy_property
    def alpha_name(self):
        """`str` The user's full name in the form of `Last name, First name`"""
        return self.__alpha_name

    @lazy_property
    def billing_codes(self):
        """`list` The billing codes against which this user has provisioning rights

        .. note::

            Only present when this user is queried in the context of an `account_id`

        """
        return self.__billing_codes

    @lazy_property
    def cloud_console_password(self):
        """`str` The encrypted password that the user can log into the underlying cloud with"""
        return self.__cloud_console_password

    @lazy_property
    def cloud_api_public_key(self):
        """`str` The encrypted public key the user can make API calls to the underlying cloud with"""
        return self.__cloud_api_public_key

    @lazy_property
    def cloud_api_secret_key(self):
        """`str` The encrypted secret key the user can make API calls to the underlying cloud with"""
        return self.__cloud_api_secret_key

    @lazy_property
    def customer(self):
        """`dict` The customer record to which this user belongs"""
        return self.__customer

    @lazy_property
    def editable(self):
        """`bool` Indicates if the core values of this user may be changed"""
        return self.__editable

    @lazy_property
    def email(self):
        """`str` Email is a unique identifier that enables a given user to
            identify themselves to enStratus
        """
        return self.__email

    @lazy_property
    def family_name(self):
        """`str` The family name of the user"""
        return self.__family_name

    @lazy_property
    def given_name(self):
        """`str` The given name of the user"""
        return self.__given_name

    @lazy_property
    def groups(self):
        """`list` The group membership of this user idependent of any individual accounts"""
        return self.__groups

    @lazy_property
    def has_cloud_api_access(self):
        """`bool` Indicates that the user has access to the underlying cloud API (i.e. AWS IAM)"""
        return self.__has_cloud_api_access

    @lazy_property
    def has_cloud_console_access(self):
        """`bool` Indicates that the user has access to the underlying cloud console (i.e. AWS IAM)"""
        return self.__has_cloud_console_access

    @lazy_property
    def notifications_targets(self):
        """`dict` The various targets configured for delivery of notifications"""
        return self.__notification_targets

    @lazy_property
    def notifications_settings(self):
        """`dict` Notification settings configured for this user"""
        return self.__notification_settings

    @lazy_property
    def status(self):
        """`str` The current status of this user in enStratus"""
        return self.__status

    @lazy_property
    def time_zone(self):
        """`str` The timezone id for the user's prefered time zone"""
        return self.__time_zone

    @lazy_property
    def vm_login_id(self):
        """`str` The username the user will use to login to cloud instances
            for shell or remote desktop access
        """
        return self.__vm_login_id

    @lazy_property
    def ssh_public_key(self):
        """`str` The public key to grant the user access to Unix instances"""
        return self.__ssh_public_key

    @classmethod
    def all(cls, keys_only=False, **kwargs):
        """Return all users

        .. note::

            The keys used to make the request determine results visibility

        :param keys_only: Return :attr:`user_id` instead of :class:`User`
        :type keys_only: bool.
        :param detail: str. The level of detail to return - `basic` or `extended`
        :type detail: str.
        :returns: `list` of :class:`User` or :attr:`user_id`
        :raises: :class:`UserException`
        """
        r = Resource(cls.PATH)
        if 'details' in kwargs:
            r.request_details = kwargs['details']
        else:
            r.request_details = 'basic'

        x = r.get()
        if r.last_error is None:
            if keys_only is True:
                return [i['user_id'] for i in x[cls.COLLECTION_NAME]]
            else:
                return [cls(i['userId']) for i in x[cls.COLLECTION_NAME]]
        else:
            raise UserException(r.last_error['error']['message'])

class UserException(BaseException): pass