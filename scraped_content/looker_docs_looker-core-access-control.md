# https://cloud.google.com/looker/docs/looker-core-access-control

Depth: 3

Looker (Google Cloud core) uses Identity and Access Management (IAM) to provision user and admin access through a set of IAM roles. For a detailed description of Google Cloud IAM, see the [IAM documentation](/iam/docs).

## What is Identity and Access Management (IAM)

IAM lets you control who has access to the resources in your Google Cloud project. IAM lets you adopt the [security principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege), so you grant only the necessary access to your resources.

Principals are the "who" of IAM. Principals can be individual users, groups, or Workspace domains. Principals are granted roles, which give them the ability to perform actions with Looker (Google Cloud core) as well as Google Cloud more generally. Each role is a collection of one or more permissions. Permissions are the basic units of IAM: each permission allows a principal to perform a certain action.

For example, the `looker.instances.login` permission lets a principal log in to Looker (Google Cloud core) instances. This permission is included in several [predefined](/iam/docs/roles-overview#role-types) roles, including the Looker Admin role (`roles/looker.admin`) and the Looker Instance User role (`roles/looker.instanceUser`).

## Required role

To get the permissions that you need to assign Looker (Google Cloud core) IAM roles, ask your administrator to grant you the [Project IAM Admin ](https://cloud.google.com/iam/docs/understanding-roles#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) IAM role on the project in which the instance was created. For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](/iam/docs/creating-custom-roles) or other [predefined roles](/iam/docs/understanding-roles). 

**Note:** [IAM basic roles](/iam/docs/understanding-roles#basic) might also contain permissions to assign Looker (Google Cloud core) IAM roles. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment. 

## IAM roles versus Looker roles

Two different kinds of roles grant permissions for Looker (Google Cloud core): IAM roles and Looker roles.

  * **Looker (Google Cloud core) IAM roles:** These kinds of roles govern the following abilities:

    * Users' capabilities within the Google Cloud console with regard to Looker (Google Cloud core)

When used together with [OAuth](/looker/docs/looker-core-oauth-authentication), they also govern the following abilities:

    * Users' abilities to sign in to a Looker (Google Cloud core) instance
    * The [default Looker role](/looker/docs/looker-core-oauth-authentication#default-role) granted to users once they log in to a Looker (Google Cloud core) instance

See the [IAM documentation](/iam/docs/manage-access-other-resources#grant-single-role) for information on how to grant IAM roles.

  * **Looker roles:** These kinds of roles govern what users can do once they sign in to a Looker (Google Cloud core) instance. See the [Roles](/looker/docs/admin-panel-users-roles) and [Groups](/looker/docs/admin-panel-users-groups) documentation pages for information on how to grant Looker roles.

When Looker roles are assigned within a Looker (Google Cloud core) instance, they override the default Looker roles that are granted by IAM.

## Looker (Google Cloud core) IAM roles

**Note:** To learn more about roles, see the [Basic and predefined roles reference](/iam/docs/understanding-roles#looker-roles).

Three predefined roles for Looker (Google Cloud core) users are available. These roles are granted at the Google Cloud project level and will control access uniformly for all Looker (Google Cloud core) instances within a Google Cloud project.

Role Name | Permissions  
---|---  
**Looker Viewer**`(roles/looker.viewer)` Read-only access to all Looker (Google Cloud core) resources. |  looker.backups.get looker.backups.list looker.instances.get looker.instances.list looker.instances.login looker.locations.get looker.locations.list looker.operations.get looker.operations.list resourcemanager.projects.get resourcemanager.projects.list  
**Looker Instance User**`roles/looker.instanceUser` Access to sign in to a Looker (Google Cloud core) instance. |  looker.instances.get looker.instances.login resourcemanager.projects.get resourcemanager.projects.list  
**Looker Admin**`roles/looker.admin` Full access to all Looker (Google Cloud core) resources. |  looker.backups.create looker.backups.delete looker.backups.get looker.backups.list looker.instances.create looker.instances.delete looker.instances.export looker.instances.get looker.instances.import looker.instances.list looker.instances.login looker.instances.update looker.locations.get looker.locations.list looker.operations.cancel looker.operations.delete looker.operations.get looker.operations.list resourcemanager.projects.get resourcemanager.projects.list  
  
At least one principal must have the Looker Admin (`roles/looker.admin`) IAM role.

If the predefined roles don't provide the set of permissions that you want, you can also create your own [custom roles](/iam/docs/creating-custom-roles).

**Warning:** The Looker Service Agent IAM role is intended only for the Looker [service account](/iam/docs/service-agents#looker-service-account) and is automatically assigned to the service account when the [Looker API is enabled](/looker/docs/looker-core-instance-create#before_you_begin). Don't grant [service agent](/iam/docs/service-agents) roles to any principals except service agents. Instead, choose a different [predefined role](/iam/docs/understanding-roles#predefined_roles), or create a [custom role](/iam/docs/understanding-custom-roles) with the permissions that you need.

## What's next

  * [Use Google OAuth for Looker (Google Cloud core) user authentication](/looker/docs/looker-core-oauth-authentication)
  * [Manage users within Looker (Google Cloud core)](/looker/docs/looker-core-user-management)
  * [Configure a Looker (Google Cloud core) instance](/looker/docs/looker-core-instance-setup)
  * [Looker (Google Cloud core) admin settings](/looker/docs/looker-core-admin-looker)
  * [Administer a Looker (Google Cloud core) instance from the Google Cloud console](/looker/docs/looker-core-admin-console)