# BigQuery API Reference

## API Resources

### REST Resource: v2.datasets

### REST Resource: v2.jobs

### REST Resource: v2.models

### REST Resource: v2.projects

### REST Resource: v2.routines

### REST Resource: v2.rowAccessPolicies

### REST Resource: v2.tabledata

### REST Resource: v2.tables

## API Endpoints

### update

**HTTP Request:** `PUT https://bigquery.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}/tables/{tableId}`

**Request Body:** The request body contains an instance of Table.

**Response Body:** If successful, the response body contains an instance of Table.

**Details:**

- **Authorization scopes:** Requires one of the following OAuth scopes:

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### getiampolicy

**HTTP Request:** `POST https://bigquery.googleapis.com/bigquery/v2/{resource=projects/*/datasets/*/tables/*}:getIamPolicy`

**Request Body:** The request body contains data with the following structure:

**Response Body:** If successful, the response body contains an instance of Policy.

**Details:**

- **Authorization scopes:** Requires one of the following OAuth scopes:

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### queryparameter

**Details:**

- **QueryParameterType:** 

- **QueryParameterValue:** 

- **RangeValue:** 

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### connectionproperty

**Details:**

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### insertall

**HTTP Request:** `POST https://bigquery.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}/tables/{tableId}/insertAll`

**Request Body:** The request body contains data with the following structure:

**Details:**

- **Authorization scopes:** Requires one of the following OAuth scopes:

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### v2_tabledata

**Details:**

- **Resource:** There is no persistent data associated with this resource.

- **Methods:** 

- **insertAll:** 

- **list:** 

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### job

**Details:**

- **JobConfiguration:** 

- **JobConfigurationQuery:** 

- **SystemVariables:** 

- **ScriptOptions:** 

- **KeyResultStatementKind:** 

- **JobConfigurationLoad:** 

- **DestinationTableProperties:** 

- **ColumnNameCharacterMap:** 

- **JobConfigurationTableCopy:** 

- **OperationType:** 

- **JobConfigurationExtract:** 

- **ModelExtractOptions:** 

- **JobStatistics:** 

- **JobStatistics2:** 

- **ExplainQueryStage:** 

- **ExplainQueryStep:** 

- **ComputeMode:** 

- **QueryTimelineSample:** 

- **MlStatistics:** 

- **TrainingType:** 

- **ExportDataStatistics:** 

- **ExternalServiceCost:** 

- **BiEngineStatistics:** 

- **BiEngineMode:** 

- **BiEngineAccelerationMode:** 

- **BiEngineReason:** 

- **Code:** 

- **LoadQueryStatistics:** 

- **SearchStatistics:** 

- **IndexUsageMode:** 

- **IndexUnusedReason:** 

- **Code:** 

- **VectorSearchStatistics:** 

- **IndexUsageMode:** 

- **StoredColumnsUsage:** 

- **StoredColumnsUnusedReason:** 

- **Code:** 

- **PerformanceInsights:** 

- **StagePerformanceStandaloneInsight:** 

- **HighCardinalityJoin:** 

- **PartitionSkew:** 

- **SkewSource:** 

- **StagePerformanceChangeInsight:** 

- **InputDataChange:** 

- **QueryInfo:** 

- **SparkStatistics:** 

- **LoggingInfo:** 

- **MaterializedViewStatistics:** 

- **MaterializedView:** 

- **RejectedReason:** 

- **MetadataCacheStatistics:** 

- **TableMetadataCacheUsage:** 

- **UnusedReason:** 

- **JobStatistics3:** 

- **JobStatistics4:** 

- **CopyJobStatistics:** 

- **ScriptStatistics:** 

- **EvaluationKind:** 

- **ScriptStackFrame:** 

- **RowLevelSecurityStatistics:** 

- **DataMaskingStatistics:** 

- **TransactionInfo:** 

- **ReservationEdition:** 

- **JobStatus:** 

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### undelete

**HTTP Request:** `POST https://bigquery.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}:undelete`

**Request Body:** The request body must be empty.

**Response Body:** If successful, the response body contains an instance of Dataset.

**Details:**

- **Authorization scopes:** Requires one of the following OAuth scopes:

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### sessioninfo

**Details:**

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### policy

**Details:**

- **Binding:** 

- **Expr:** 

- **AuditConfig:** 

- **AuditLogConfig:** 

- **LogType:** 

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### dataformatoptions

**Details:**

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### tablereference

**Details:**

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### projectreference

**Details:**

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### overview

**Details:**

- **Resource: Table:** 

- **TableSchema:** 

- **TableFieldSchema:** 

- **FieldElementType:** 

- **TimePartitioning:** 

- **RangePartitioning:** 

- **Clustering:** 

- **PartitioningDefinition:** 

- **PartitionedColumn:** 

- **ViewDefinition:** 

- **UserDefinedFunctionResource:** 

- **PrivacyPolicy:** 

- **AggregationThresholdPolicy:** 

- **MaterializedViewDefinition:** 

- **MaterializedViewStatus:** 

- **ErrorProto:** 

- **ExternalDataConfiguration:** 

- **FileSetSpecType:** 

- **CsvOptions:** 

- **JsonOptions:** 

- **BigtableOptions:** 

- **BigtableColumnFamily:** 

- **BigtableColumn:** 

- **GoogleSheetsOptions:** 

- **HivePartitioningOptions:** 

- **DecimalTargetType:** 

- **AvroOptions:** 

- **JsonExtension:** 

- **ParquetOptions:** 

- **MapTargetType:** 

- **ObjectMetadata:** 

- **MetadataCacheMode:** 

- **BigLakeConfiguration:** 

- **FileFormat:** 

- **TableFormat:** 

- **Streamingbuffer:** 

- **SnapshotDefinition:** 

- **CloneDefinition:** 

- **TableConstraints:** 

- **PrimaryKey:** 

- **ForeignKey:** 

- **ColumnReference:** 

- **ExternalCatalogTableOptions:** 

- **StorageDescriptor:** 

- **SerDeInfo:** 

- **Methods:** 

- **delete:** 

- **get:** 

- **getIamPolicy:** 

- **insert:** 

- **list:** 

- **patch:** 

- **setIamPolicy:** 

- **testIamPermissions:** 

- **update:** 

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### v2_tables

**Details:**

- **Resource: Table:** 

- **TableSchema:** 

- **TableFieldSchema:** 

- **FieldElementType:** 

- **TimePartitioning:** 

- **RangePartitioning:** 

- **Clustering:** 

- **PartitioningDefinition:** 

- **PartitionedColumn:** 

- **ViewDefinition:** 

- **UserDefinedFunctionResource:** 

- **PrivacyPolicy:** 

- **AggregationThresholdPolicy:** 

- **MaterializedViewDefinition:** 

- **MaterializedViewStatus:** 

- **ErrorProto:** 

- **ExternalDataConfiguration:** 

- **FileSetSpecType:** 

- **CsvOptions:** 

- **JsonOptions:** 

- **BigtableOptions:** 

- **BigtableColumnFamily:** 

- **BigtableColumn:** 

- **GoogleSheetsOptions:** 

- **HivePartitioningOptions:** 

- **DecimalTargetType:** 

- **AvroOptions:** 

- **JsonExtension:** 

- **ParquetOptions:** 

- **MapTargetType:** 

- **ObjectMetadata:** 

- **MetadataCacheMode:** 

- **BigLakeConfiguration:** 

- **FileFormat:** 

- **TableFormat:** 

- **Streamingbuffer:** 

- **SnapshotDefinition:** 

- **CloneDefinition:** 

- **TableConstraints:** 

- **PrimaryKey:** 

- **ForeignKey:** 

- **ColumnReference:** 

- **ExternalCatalogTableOptions:** 

- **StorageDescriptor:** 

- **SerDeInfo:** 

- **Methods:** 

- **delete:** 

- **get:** 

- **getIamPolicy:** 

- **insert:** 

- **list:** 

- **patch:** 

- **setIamPolicy:** 

- **testIamPermissions:** 

- **update:** 

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### dmlstats

**Details:**

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### list

**HTTP Request:** `GET https://bigquery.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}/tables`

**Request Body:** The request body must be empty.

**Details:**

- **Authorization scopes:** Requires one of the following OAuth scopes:

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### getserviceaccount

**HTTP Request:** `GET https://bigquery.googleapis.com/bigquery/v2/projects/{projectId}/serviceAccount`

**Request Body:** The request body must be empty.

**Details:**

- **Authorization scopes:** Requires one of the following OAuth scopes:

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### v2_models

**Details:**

- **Resource: Model:** 

- **ModelReference:** 

- **ModelType:** 

- **TrainingRun:** 

- **TrainingOptions:** 

- **LossType:** 

- **DataSplitMethod:** 

- **LearnRateStrategy:** 

- **DistanceType:** 

- **OptimizationStrategy:** 

- **BoosterType:** 

- **DartNormalizeType:** 

- **TreeMethod:** 

- **FeedbackType:** 

- **KmeansInitializationMethod:** 

- **ArimaOrder:** 

- **DataFrequency:** 

- **HolidayRegion:** 

- **HparamTuningObjective:** 

- **EncodingMethod:** 

- **PcaSolver:** 

- **ModelRegistry:** 

- **IterationResult:** 

- **ClusterInfo:** 

- **ArimaResult:** 

- **ArimaModelInfo:** 

- **ArimaCoefficients:** 

- **ArimaFittingMetrics:** 

- **SeasonalPeriodType:** 

- **PrincipalComponentInfo:** 

- **EvaluationMetrics:** 

- **RegressionMetrics:** 

- **BinaryClassificationMetrics:** 

- **AggregateClassificationMetrics:** 

- **BinaryConfusionMatrix:** 

- **MultiClassClassificationMetrics:** 

- **ConfusionMatrix:** 

- **Row:** 

- **Entry:** 

- **ClusteringMetrics:** 

- **Cluster:** 

- **FeatureValue:** 

- **CategoricalValue:** 

- **CategoryCount:** 

- **RankingMetrics:** 

- **ArimaForecastingMetrics:** 

- **ArimaSingleModelForecastingMetrics:** 

- **DimensionalityReductionMetrics:** 

- **DataSplitResult:** 

- **GlobalExplanation:** 

- **Explanation:** 

- **TransformColumn:** 

- **HparamSearchSpaces:** 

- **DoubleHparamSearchSpace:** 

- **DoubleRange:** 

- **DoubleCandidates:** 

- **IntHparamSearchSpace:** 

- **IntRange:** 

- **IntCandidates:** 

- **IntArrayHparamSearchSpace:** 

- **IntArray:** 

- **StringHparamSearchSpace:** 

- **HparamTuningTrial:** 

- **TrialStatus:** 

- **RemoteModelInfo:** 

- **RemoteServiceType:** 

- **Methods:** 

- **delete:** 

- **get:** 

- **list:** 

- **patch:** 

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### get

**HTTP Request:** `GET https://bigquery.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}/tables/{tableId}`

**Request Body:** The request body must be empty.

**Response Body:** If successful, the response body contains an instance of Table.

**Details:**

- **Authorization scopes:** Requires one of the following OAuth scopes:

- **TableMetadataView:** 

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### v2_datasets

**Details:**

- **Resource: Dataset:** 

- **DatasetReference:** 

- **LinkedDatasetSource:** 

- **LinkedDatasetMetadata:** 

- **LinkState:** 

- **ExternalDatasetReference:** 

- **ExternalCatalogDatasetOptions:** 

- **GcpTag:** 

- **StorageBillingModel:** 

- **Methods:** 

- **delete:** 

- **get:** 

- **insert:** 

- **list:** 

- **patch:** 

- **undelete:** 

- **update:** 

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### standardsqlfield

**Details:**

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### v2_projects

**Details:**

- **Resource:** There is no persistent data associated with this resource.

- **Methods:** 

- **getServiceAccount:** 

- **list:** 

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### datasetaccessentry

**Details:**

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### getpolicyoptions

**Details:**

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### cancel

**HTTP Request:** `POST https://bigquery.googleapis.com/bigquery/v2/projects/{projectId}/jobs/{jobId}/cancel`

**Request Body:** The request body must be empty.

**Details:**

- **Authorization scopes:** Requires one of the following OAuth scopes:

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### setiampolicy

**HTTP Request:** `POST https://bigquery.googleapis.com/bigquery/v2/{resource=projects/*/datasets/*/tables/*}:setIamPolicy`

**Request Body:** The request body contains data with the following structure:

**Response Body:** If successful, the response body contains an instance of Policy.

**Details:**

- **Authorization scopes:** Requires one of the following OAuth scopes:

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### testiampermissionsresponse

**Details:**

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### targettype

**Details:**

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### patch

**HTTP Request:** `PATCH https://bigquery.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}/tables/{tableId}`

**Request Body:** The request body contains an instance of Table.

**Response Body:** If successful, the response body contains an instance of Table.

**Details:**

- **Authorization scopes:** Requires one of the following OAuth scopes:

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### query

**HTTP Request:** `POST https://bigquery.googleapis.com/bigquery/v2/projects/{projectId}/queries`

**Request Body:** The request body contains an instance of QueryRequest.

**Details:**

- **Authorization scopes:** Requires one of the following OAuth scopes:

- **QueryRequest:** 

- **JobCreationMode:** 

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### v2_routines

**Details:**

- **Resource: Routine:** 

- **RoutineReference:** 

- **RoutineType:** 

- **Language:** 

- **Argument:** 

- **ArgumentKind:** 

- **Mode:** 

- **StandardSqlTableType:** 

- **DeterminismLevel:** 

- **RemoteFunctionOptions:** 

- **SparkOptions:** 

- **DataGovernanceType:** 

- **Methods:** 

- **delete:** 

- **get:** 

- **insert:** 

- **list:** 

- **update:** 

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### testiampermissions

**HTTP Request:** `POST https://bigquery.googleapis.com/bigquery/v2/{resource=projects/*/datasets/*/tables/*}:testIamPermissions`

**Request Body:** The request body contains data with the following structure:

**Response Body:** If successful, the response body contains an instance of TestIamPermissionsResponse.

**Details:**

- **Authorization scopes:** Requires one of the following OAuth scopes:

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### delete

**HTTP Request:** `DELETE https://bigquery.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}/tables/{tableId}`

**Request Body:** The request body must be empty.

**Response Body:** If successful, the response body is an empty JSON object.

**Details:**

- **Authorization scopes:** Requires one of the following OAuth scopes:

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### getqueryresults

**HTTP Request:** `GET https://bigquery.googleapis.com/bigquery/v2/projects/{projectId}/queries/{jobId}`

**Request Body:** The request body must be empty.

**Details:**

- **Authorization scopes:** Requires one of the following OAuth scopes:

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### standardsqldatatype

**Details:**

- **TypeKind:** 

- **StandardSqlStructType:** 

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### encryptionconfiguration

**Details:**

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### jobreference

**Details:**

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### insert

**HTTP Request:** `POST https://bigquery.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}/tables`

**Request Body:** The request body contains an instance of Table.

**Response Body:** If successful, the response body contains a newly created instance of Table.

**Details:**

- **Authorization scopes:** Requires one of the following OAuth scopes:

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### roundingmode

**Details:**

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### jobcreationreason

**Details:**

- **Code:** 

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### v2_rowaccesspolicies

**Details:**

- **Resource: RowAccessPolicy:** 

- **RowAccessPolicyReference:** 

- **Methods:** 

- **getIamPolicy:** 

- **list:** 

- **testIamPermissions:** 

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### v2_jobs

**Details:**

- **Resource:** There is no persistent data associated with this resource.

- **Methods:** 

- **cancel:** 

- **delete:** 

- **get:** 

- **getQueryResults:** 

- **insert:** 

- **list:** 

- **query:** 

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

