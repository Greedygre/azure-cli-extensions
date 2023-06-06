# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['dataprotection'] = '''
    type: group
    short-summary: Manage Data Protection
'''

helps['dataprotection backup-policy'] = """
    type: group
    short-summary: Manage backup policy with dataprotection
"""

helps['dataprotection backup-policy list'] = """
    type: command
    short-summary: "Returns list of backup policies belonging to a backup vault."
    examples:
      - name: List BackupPolicy
        text: |-
               az dataprotection backup-policy list --resource-group "000pikumar" --vault-name "PrivatePreviewVault"
"""

helps['dataprotection backup-policy show'] = """
    type: command
    short-summary: "Gets a backup policy belonging to a backup vault."
    examples:
      - name: Get BackupPolicy
        text: |-
               az dataprotection backup-policy show --name "OSSDBPolicy" --resource-group "000pikumar" --vault-name \
"PrivatePreviewVault"
"""

helps['dataprotection backup-policy create'] = """
    type: command
    short-summary: "Create a backup policy belonging to a backup vault."
    parameters:
      - name: --backup-policy
        short-summary: "Rule based backup policy"
        long-summary: |
            Usage: --backup-policy policy-rules=XX datasource-types=XX object-type=XX

            policy-rules: Required. Policy rule dictionary that contains rules for each backuptype i.e \
Full/Incremental/Logs etc
            datasource-types: Required. Type of datasource for the backup management
    examples:
      - name: CreateOrUpdate BackupPolicy
        text: |-
               az dataprotection backup-policy create --name "OSSDBPolicy" --properties "{\\"datasourceTypes\\":[\\"Oss\
DB\\"],\\"objectType\\":\\"BackupPolicy\\",\\"policyRules\\":[{\\"name\\":\\"BackupWeekly\\",\\"backupParameters\\":{\\\
"backupType\\":\\"Full\\",\\"objectType\\":\\"AzureBackupParams\\"},\\"dataStore\\":{\\"dataStoreType\\":\\"VaultStore\
\\",\\"objectType\\":\\"DataStoreInfoBase\\"},\\"objectType\\":\\"AzureBackupRule\\",\\"trigger\\":{\\"objectType\\":\\\
"ScheduleBasedTriggerContext\\",\\"schedule\\":{\\"repeatingTimeIntervals\\":[\\"R/2019-11-20T08:00:00-08:00/P1W\\"]},\
\\"taggingCriteria\\":[{\\"isDefault\\":true,\\"tagInfo\\":{\\"tagName\\":\\"Default\\"},\\"taggingPriority\\":99},{\\"\
criteria\\":[{\\"daysOfTheWeek\\":[\\"Sunday\\"],\\"objectType\\":\\"ScheduleBasedBackupCriteria\\",\\"scheduleTimes\\"\
:[\\"2019-03-01T13:00:00Z\\"]}],\\"isDefault\\":false,\\"tagInfo\\":{\\"tagName\\":\\"Weekly\\"},\\"taggingPriority\\":\
20}]}},{\\"name\\":\\"Default\\",\\"isDefault\\":true,\\"lifecycles\\":[{\\"deleteAfter\\":{\\"duration\\":\\"P1W\\",\\\
"objectType\\":\\"AbsoluteDeleteOption\\"},\\"sourceDataStore\\":{\\"dataStoreType\\":\\"VaultStore\\",\\"objectType\\"\
:\\"DataStoreInfoBase\\"}}],\\"objectType\\":\\"AzureRetentionRule\\"},{\\"name\\":\\"Weekly\\",\\"isDefault\\":false,\
\\"lifecycles\\":[{\\"deleteAfter\\":{\\"duration\\":\\"P12W\\",\\"objectType\\":\\"AbsoluteDeleteOption\\"},\\"sourceD\
ataStore\\":{\\"dataStoreType\\":\\"VaultStore\\",\\"objectType\\":\\"DataStoreInfoBase\\"}}],\\"objectType\\":\\"Azure\
RetentionRule\\"}]}" --resource-group "000pikumar" --vault-name "PrivatePreviewVault"
"""

helps['dataprotection backup-policy delete'] = """
    type: command
    short-summary: "Deletes a backup policy belonging to a backup vault."
    examples:
      - name: Delete BackupPolicy
        text: |-
               az dataprotection backup-policy delete --name "OSSDBPolicy" --resource-group "000pikumar" --vault-name \
"PrivatePreviewVault"
"""

helps['dataprotection backup-instance'] = """
    type: group
    short-summary: Manage backup instance with dataprotection
"""

helps['dataprotection backup-instance list'] = """
    type: command
    short-summary: "Gets a backup instances belonging to a backup vault."
    examples:
      - name: List BackupInstances in a Vault
        text: |-
               az dataprotection backup-instance list --resource-group "000pikumar" --vault-name \
"PratikPrivatePreviewVault1"
"""

helps['dataprotection backup-instance show'] = """
    type: command
    short-summary: "Gets a backup instance with name in a backup vault."
    examples:
      - name: Get BackupInstance
        text: |-
               az dataprotection backup-instance show --name "testInstance1" --resource-group "000pikumar" \
--vault-name "PratikPrivatePreviewVault1"
"""

helps['dataprotection backup-instance create'] = """
    type: command
    short-summary: "Create a backup instance in a backup vault."
    parameters:
      - name: --data-source-info
        short-summary: "Gets or sets the data source information."
        long-summary: |
            Usage: --data-source-info datasource-type=XX object-type=XX resource-id=XX resource-location=XX \
resource-name=XX resource-type=XX resource-uri=XX

            datasource-type: DatasourceType of the resource.
            object-type: Type of Datasource object, used to initialize the right inherited type
            resource-id: Required. Full ARM ID of the resource. For azure resources, this is ARM ID. For non azure \
resources, this will be the ID created by backup service via Fabric/Vault.
            resource-location: Location of datasource.
            resource-name: Unique identifier of the resource in the context of parent.
            resource-type: Resource Type of Datasource.
            resource-uri: Uri of the resource.
      - name: --data-source-set-info
        short-summary: "Gets or sets the data source set information."
        long-summary: |
            Usage: --data-source-set-info datasource-type=XX object-type=XX resource-id=XX resource-location=XX \
resource-name=XX resource-type=XX resource-uri=XX

            datasource-type: DatasourceType of the resource.
            object-type: Type of Datasource object, used to initialize the right inherited type
            resource-id: Required. Full ARM ID of the resource. For azure resources, this is ARM ID. For non azure \
resources, this will be the ID created by backup service via Fabric/Vault.
            resource-location: Location of datasource.
            resource-name: Unique identifier of the resource in the context of parent.
            resource-type: Resource Type of Datasource.
            resource-uri: Uri of the resource.
      - name: --secret-store-based-auth-credentials
        short-summary: "Secret store based authentication credentials."
        long-summary: |
            Usage: --secret-store-based-auth-credentials uri=XX secret-store-type=XX value=XX object-type=XX

            uri: Uri to get to the resource
            secret-store-type: Gets or sets the type of secret store
            value: Gets or sets value stored in secret store resource
            object-type: Required. Type of the specific object - used for deserializing
      - name: --policy-parameters
        short-summary: "Policy parameters for the backup instance"
        long-summary: |
            Usage: --policy-parameters data-store-parameters-list=XX

            data-store-parameters-list: Gets or sets the DataStore Parameters
    examples:
      - name: Create BackupInstance
        text: |-
               az dataprotection backup-instance create --name "testInstance1" --data-source-info \
datasource-type="Microsoft.DBforPostgreSQL/servers/databases" object-type="Datasource" resource-id="/subscriptions/f75d\
8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/viveksipgtest/providers/Microsoft.DBforPostgreSQL/servers/viveksipgtest\
/databases/testdb" resource-location="" resource-name="testdb" resource-type="Microsoft.DBforPostgreSQL/servers/databas\
es" resource-uri="" --data-source-set-info datasource-type="Microsoft.DBforPostgreSQL/servers/databases" \
object-type="DatasourceSet" resource-id="/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/viveksipgte\
st/providers/Microsoft.DBforPostgreSQL/servers/viveksipgtest" resource-location="" resource-name="viveksipgtest" \
resource-type="Microsoft.DBforPostgreSQL/servers" resource-uri="" --policy-parameters objectType="SecretStoreBasedAuthC\
redentials" secretStoreResource={"secretStoreType":"AzureKeyVault","uri":"https://samplevault.vault.azure.net/secrets/c\
redentials"} --friendly-name "harshitbi2" --object-type "BackupInstance" --policy-id "/subscriptions/04cf684a-d41f-4550\
-9f70-7708a3a2283b/resourceGroups/000pikumar/providers/Microsoft.DataProtection/Backupvaults/PratikPrivatePreviewVault1\
/backupPolicies/PratikPolicy1" --policy-parameters data-store-parameters-list={"dataStoreType":"OperationalStore","obje\
ctType":"AzureOperationalStoreParameters","resourceGroupId":"/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resour\
ceGroups/viveksipgtest"} --validation-type "ShallowValidation" --tags key1="val1" --resource-group "000pikumar" \
--vault-name "PratikPrivatePreviewVault1"
"""

helps['dataprotection backup-instance delete'] = """
    type: command
    short-summary: "Delete a backup instance in a backup vault."
    examples:
      - name: Delete BackupInstance
        text: |-
               az dataprotection backup-instance delete --name "testInstance1" --resource-group "000pikumar" \
--vault-name "PratikPrivatePreviewVault1"
"""

helps['dataprotection backup-instance adhoc-backup'] = """
    type: command
    short-summary: "Trigger adhoc backup."
    examples:
      - name: Trigger Adhoc Backup
        text: |-
               az dataprotection backup-instance adhoc-backup --name "testInstance1" --rule-name "BackupWeekly" \
--retention-tag-override "yearly" --resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1"
"""

helps['dataprotection backup-instance restore'] = """
    type: group
    short-summary: Manage backup instance with dataprotection sub group restore
"""

helps['dataprotection backup-instance restore trigger'] = """
    type: command
    short-summary: "Triggers restore for a BackupInstance."
    examples:
      - name: Trigger Restore
        text: |-
               az dataprotection backup-instance restore trigger --name "testInstance1" --restore-request-object \
"{\\"objectType\\":\\"AzureBackupRecoveryPointBasedRestoreRequest\\",\\"recoveryPointId\\":\\"hardcodedRP\\",\\"restore\
TargetInfo\\":{\\"datasourceAuthCredentials\\":{\\"objectType\\":\\"SecretStoreBasedAuthCredentials\\",\\"secretStoreRe\
source\\":{\\"secretStoreType\\":\\"AzureKeyVault\\",\\"uri\\":\\"https://samplevault.vault.azure.net/secrets/credentia\
ls\\"}},\\"datasourceInfo\\":{\\"datasourceType\\":\\"Microsoft.DBforPostgreSQL/servers/databases\\",\\"objectType\\":\
\\"Datasource\\",\\"resourceID\\":\\"/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/viveksipgtest/p\
roviders/Microsoft.DBforPostgreSQL/servers/viveksipgtest/databases/targetdb\\",\\"resourceLocation\\":\\"\\",\\"resourc\
eName\\":\\"targetdb\\",\\"resourceType\\":\\"Microsoft.DBforPostgreSQL/servers/databases\\",\\"resourceUri\\":\\"\\"},\
\\"datasourceSetInfo\\":{\\"datasourceType\\":\\"Microsoft.DBforPostgreSQL/servers/databases\\",\\"objectType\\":\\"Dat\
asourceSet\\",\\"resourceID\\":\\"/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/viveksipgtest/prov\
iders/Microsoft.DBforPostgreSQL/servers/viveksipgtest\\",\\"resourceLocation\\":\\"\\",\\"resourceName\\":\\"viveksipgt\
est\\",\\"resourceType\\":\\"Microsoft.DBforPostgreSQL/servers\\",\\"resourceUri\\":\\"\\"},\\"objectType\\":\\"Restore\
TargetInfo\\",\\"recoveryOption\\":\\"FailIfExists\\",\\"restoreLocation\\":\\"southeastasia\\"},\\"sourceDataStoreType\
\\":\\"VaultStore\\",\\"sourceResourceId\\":\\"/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/vivek\
sipgtest/providers/Microsoft.DBforPostgreSQL/servers/viveksipgtest/databases/testdb\\"}" --resource-group "000pikumar" \
--vault-name "PratikPrivatePreviewVault1"
      - name: Trigger Restore As Files
        text: |-
               az dataprotection backup-instance restore trigger --name "testInstance1" --restore-request-object \
"{\\"objectType\\":\\"AzureBackupRecoveryPointBasedRestoreRequest\\",\\"recoveryPointId\\":\\"hardcodedRP\\",\\"restore\
TargetInfo\\":{\\"objectType\\":\\"RestoreFilesTargetInfo\\",\\"recoveryOption\\":\\"FailIfExists\\",\\"restoreLocation\
\\":\\"southeastasia\\",\\"targetDetails\\":{\\"filePrefix\\":\\"restoredblob\\",\\"restoreTargetLocationType\\":\\"Azu\
reBlobs\\",\\"url\\":\\"https://teststorage.blob.core.windows.net/restoretest\\"}},\\"sourceDataStoreType\\":\\"VaultSt\
ore\\",\\"sourceResourceId\\":\\"/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/viveksipgtest/provi\
ders/Microsoft.DBforPostgreSQL/servers/viveksipgtest/databases/testdb\\"}" --resource-group "000pikumar" --vault-name \
"PrivatePreviewVault1"
      - name: Trigger Restore With Rehydration
        text: |-
               az dataprotection backup-instance restore trigger --name "testInstance1" --restore-request-object \
"{\\"objectType\\":\\"AzureBackupRestoreWithRehydrationRequest\\",\\"recoveryPointId\\":\\"hardcodedRP\\",\\"rehydratio\
nPriority\\":\\"High\\",\\"rehydrationRetentionDuration\\":\\"7D\\",\\"restoreTargetInfo\\":{\\"datasourceInfo\\":{\\"d\
atasourceType\\":\\"OssDB\\",\\"objectType\\":\\"Datasource\\",\\"resourceID\\":\\"/subscriptions/f75d8d8b-6735-4697-82\
e1-1a7a3ff0d5d4/resourceGroups/viveksipgtest/providers/Microsoft.DBforPostgreSQL/servers/viveksipgtest/databases/testdb\
\\",\\"resourceLocation\\":\\"\\",\\"resourceName\\":\\"testdb\\",\\"resourceType\\":\\"Microsoft.DBforPostgreSQL/serve\
rs/databases\\",\\"resourceUri\\":\\"\\"},\\"datasourceSetInfo\\":{\\"datasourceType\\":\\"OssDB\\",\\"objectType\\":\\\
"DatasourceSet\\",\\"resourceID\\":\\"/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/viveksipgtest/\
providers/Microsoft.DBforPostgreSQL/servers/viveksipgtest\\",\\"resourceLocation\\":\\"\\",\\"resourceName\\":\\"viveks\
ipgtest\\",\\"resourceType\\":\\"Microsoft.DBforPostgreSQL/servers\\",\\"resourceUri\\":\\"\\"},\\"objectType\\":\\"Res\
toreTargetInfo\\",\\"recoveryOption\\":\\"FailIfExists\\",\\"restoreLocation\\":\\"southeastasia\\"},\\"sourceDataStore\
Type\\":\\"VaultStore\\",\\"sourceResourceId\\":\\"/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/v\
iveksipgtest/providers/Microsoft.DBforPostgreSQL/servers/viveksipgtest/databases/testdb\\"}" --resource-group \
"000pikumar" --vault-name "PratikPrivatePreviewVault1"
"""

helps['dataprotection backup-instance resume-protection'] = """
    type: command
    short-summary: "This operation will resume protection for a stopped backup instance."
    examples:
      - name: ResumeProtection
        text: |-
               az dataprotection backup-instance resume-protection --name "testbi" --resource-group "testrg" \
--vault-name "testvault"
"""

helps['dataprotection backup-instance stop-protection'] = """
    type: command
    short-summary: "This operation will stop protection of a backup instance and data will be held forever."
    examples:
      - name: StopProtection
        text: |-
               az dataprotection backup-instance stop-protection --name "testbi" --resource-group "testrg" \
--vault-name "testvault"
"""

helps['dataprotection backup-instance suspend-backup'] = """
    type: command
    short-summary: "This operation will stop backups for backup instance."
    examples:
      - name: SuspendBackups
        text: |-
               az dataprotection backup-instance suspend-backup --name "testbi" --resource-group "testrg" --vault-name \
"testvault"
"""

helps['dataprotection backup-instance validate-for-backup'] = """
    type: command
    short-summary: "Validate whether adhoc backup will be successful or not."
    parameters:
      - name: --data-source-info
        short-summary: "Gets or sets the data source information."
        long-summary: |
            Usage: --data-source-info datasource-type=XX object-type=XX resource-id=XX resource-location=XX \
resource-name=XX resource-type=XX resource-uri=XX

            datasource-type: DatasourceType of the resource.
            object-type: Type of Datasource object, used to initialize the right inherited type
            resource-id: Required. Full ARM ID of the resource. For azure resources, this is ARM ID. For non azure \
resources, this will be the ID created by backup service via Fabric/Vault.
            resource-location: Location of datasource.
            resource-name: Unique identifier of the resource in the context of parent.
            resource-type: Resource Type of Datasource.
            resource-uri: Uri of the resource.
      - name: --data-source-set-info
        short-summary: "Gets or sets the data source set information."
        long-summary: |
            Usage: --data-source-set-info datasource-type=XX object-type=XX resource-id=XX resource-location=XX \
resource-name=XX resource-type=XX resource-uri=XX

            datasource-type: DatasourceType of the resource.
            object-type: Type of Datasource object, used to initialize the right inherited type
            resource-id: Required. Full ARM ID of the resource. For azure resources, this is ARM ID. For non azure \
resources, this will be the ID created by backup service via Fabric/Vault.
            resource-location: Location of datasource.
            resource-name: Unique identifier of the resource in the context of parent.
            resource-type: Resource Type of Datasource.
            resource-uri: Uri of the resource.
      - name: --secret-store-based-auth-credentials
        short-summary: "Secret store based authentication credentials."
        long-summary: |
            Usage: --secret-store-based-auth-credentials uri=XX secret-store-type=XX value=XX object-type=XX

            uri: Uri to get to the resource
            secret-store-type: Gets or sets the type of secret store
            value: Gets or sets value stored in secret store resource
            object-type: Required. Type of the specific object - used for deserializing
      - name: --policy-parameters
        short-summary: "Policy parameters for the backup instance"
        long-summary: |
            Usage: --policy-parameters data-store-parameters-list=XX

            data-store-parameters-list: Gets or sets the DataStore Parameters
    examples:
      - name: Validate For Backup
        text: |-
               az dataprotection backup-instance validate-for-backup --data-source-info datasource-type="OssDB" \
object-type="Datasource" resource-id="/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/viveksipgtest/\
providers/Microsoft.DBforPostgreSQL/servers/viveksipgtest/databases/testdb" resource-location="" \
resource-name="testdb" resource-type="Microsoft.DBforPostgreSQL/servers/databases" resource-uri="" \
--data-source-set-info datasource-type="OssDB" object-type="DatasourceSet" resource-id="/subscriptions/f75d8d8b-6735-46\
97-82e1-1a7a3ff0d5d4/resourceGroups/viveksipgtest/providers/Microsoft.DBforPostgreSQL/servers/viveksipgtest" \
resource-location="" resource-name="viveksipgtest" resource-type="Microsoft.DBforPostgreSQL/servers" resource-uri="" \
--policy-parameters objectType="SecretStoreBasedAuthCredentials" secretStoreResource={"secretStoreType":"AzureKeyVault"\
,"uri":"https://samplevault.vault.azure.net/secrets/credentials"} --friendly-name "harshitbi2" --object-type \
"BackupInstance" --policy-id "/subscriptions/04cf684a-d41f-4550-9f70-7708a3a2283b/resourceGroups/000pikumar/providers/M\
icrosoft.DataProtection/Backupvaults/PratikPrivatePreviewVault1/backupPolicies/PratikPolicy1" --resource-group \
"000pikumar" --vault-name "PratikPrivatePreviewVault1"
"""

helps['dataprotection backup-instance validate-for-restore'] = """
    type: command
    short-summary: "Validates if Restore can be triggered for a DataSource."
    examples:
      - name: Validate Restore
        text: |-
               az dataprotection backup-instance validate-for-restore --name "testInstance1" --restore-request-object \
"{\\"objectType\\":\\"AzureBackupRecoveryPointBasedRestoreRequest\\",\\"recoveryPointId\\":\\"hardcodedRP\\",\\"restore\
TargetInfo\\":{\\"datasourceAuthCredentials\\":{\\"objectType\\":\\"SecretStoreBasedAuthCredentials\\",\\"secretStoreRe\
source\\":{\\"secretStoreType\\":\\"AzureKeyVault\\",\\"uri\\":\\"https://samplevault.vault.azure.net/secrets/credentia\
ls\\"}},\\"datasourceInfo\\":{\\"datasourceType\\":\\"Microsoft.DBforPostgreSQL/servers/databases\\",\\"objectType\\":\
\\"Datasource\\",\\"resourceID\\":\\"/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/viveksipgtest/p\
roviders/Microsoft.DBforPostgreSQL/servers/viveksipgtest/databases/targetdb\\",\\"resourceLocation\\":\\"\\",\\"resourc\
eName\\":\\"targetdb\\",\\"resourceType\\":\\"Microsoft.DBforPostgreSQL/servers/databases\\",\\"resourceUri\\":\\"\\"},\
\\"datasourceSetInfo\\":{\\"datasourceType\\":\\"Microsoft.DBforPostgreSQL/servers/databases\\",\\"objectType\\":\\"Dat\
asourceSet\\",\\"resourceID\\":\\"/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/viveksipgtest/prov\
iders/Microsoft.DBforPostgreSQL/servers/viveksipgtest\\",\\"resourceLocation\\":\\"\\",\\"resourceName\\":\\"viveksipgt\
est\\",\\"resourceType\\":\\"Microsoft.DBforPostgreSQL/servers\\",\\"resourceUri\\":\\"\\"},\\"objectType\\":\\"Restore\
TargetInfo\\",\\"recoveryOption\\":\\"FailIfExists\\",\\"restoreLocation\\":\\"southeastasia\\"},\\"sourceDataStoreType\
\\":\\"VaultStore\\",\\"sourceResourceId\\":\\"/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/vivek\
sipgtest/providers/Microsoft.DBforPostgreSQL/servers/viveksipgtest/databases/testdb\\"}" --resource-group "000pikumar" \
--vault-name "PratikPrivatePreviewVault1"
"""

helps['dataprotection backup-instance wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the dataprotection backup-instance is met.
    examples:
      - name: Pause executing next line of CLI script until the dataprotection backup-instance is successfully \
created.
        text: |-
               az dataprotection backup-instance wait --name "testInstance1" --resource-group "000pikumar" \
--vault-name "PratikPrivatePreviewVault1" --created
      - name: Pause executing next line of CLI script until the dataprotection backup-instance is successfully \
deleted.
        text: |-
               az dataprotection backup-instance wait --name "testInstance1" --resource-group "000pikumar" \
--vault-name "PratikPrivatePreviewVault1" --deleted
"""

helps['dataprotection restorable-time-range'] = """
    type: group
    short-summary: Manage restorable time range with dataprotection
"""

helps['dataprotection restorable-time-range find'] = """
    type: command
    short-summary: "."
    examples:
      - name: Find Restorable Time Ranges
        text: |-
               az dataprotection restorable-time-range find --backup-instance-name "zblobbackuptestsa58" --end-time \
"2021-02-24T00:35:17.6829685Z" --source-data-store-type "OperationalStore" --start-time "2020-10-17T23:28:17.6829685Z" \
--resource-group "Blob-Backup" --vault-name "ZBlobBackupVaultBVTD3"
"""

helps['dataprotection resource-guard'] = """
    type: group
    short-summary: Manage resource guard with dataprotection
"""

helps['dataprotection resource-guard show'] = """
    type: command
    short-summary: "Returns a ResourceGuard belonging to a resource group."
    examples:
      - name: Get ResourceGuard
        text: |-
               az dataprotection resource-guard show --resource-group "SampleResourceGroup" --resource-guard-name \
"swaggerExample"
"""

helps['dataprotection resource-guard create'] = """
    type: command
    short-summary: "Creates or updates a ResourceGuard resource belonging to a resource group."
    examples:
      - name: Create ResourceGuard
        text: |-
               az dataprotection resource-guard create --location "WestUS" --tags key1="val1" --resource-group \
"SampleResourceGroup" --resource-guard-name "swaggerExample"
"""

helps['dataprotection resource-guard delete'] = """
    type: command
    short-summary: "Deletes a ResourceGuard resource from the resource group."
    examples:
      - name: Delete ResourceGuard
        text: |-
               az dataprotection resource-guard delete --resource-group "SampleResourceGroup" --resource-guard-name \
"swaggerExample"
"""
