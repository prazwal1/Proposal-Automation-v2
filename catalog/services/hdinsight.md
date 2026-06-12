# Hdinsight

- slug: `hdinsight`  |  module: `hdinsight-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Component`** (select)
  - options: Hadoop, Spark, Interactive Query, HDInsight Machine Learning Services, Kafka, HBase, Storm

- **`Category`** (select)
  - depends on: `cluster`
  - options: All, General Purpose, Optimized

- **`Instance Series`** (select)
  - depends on: `cluster`, `headCategory`
  - options: All, A-Series, AV2-Series, DV2-Series, EV3-Series
  - when `cluster` = *Interactive Query*: All, AV2-Series, DV2-Series, EV3-Series
  - when `headCategory` = *General Purpose*: All, A-Series, AV2-Series, DV2-Series
  - when `headCategory` = *Optimized*: All, DV2-Series, EV3-Series

- **`Instance: (Need help finding the right VM?)`** (text)

- **`Hours`** (number)
  - depends on: `cluster`

- **`headHoursFactor`** (select)
  - depends on: `cluster`
  - options: Hours, Days, Month

- **`workerCategory`** (select)
  - depends on: `cluster`
  - options: All, General Purpose, Optimized
  - when `cluster` = *HDInsight Machine Learning Services*: All, Compute Optimized, General Purpose, Optimized

- **`workerInstanceSeries`** (select)
  - depends on: `cluster`, `workerCategory`
  - options: All, A-Series, AV2-Series, DV2-Series, EV3-Series
  - when `cluster` = *Interactive Query*: All, AV2-Series, DV2-Series, EV3-Series
  - when `cluster` = *HDInsight Machine Learning Services*: All, A-Series, AV2-Series, DV2-Series, EV3-Series, F-Series
  - when `workerCategory` = *General Purpose*: All, A-Series, AV2-Series, DV2-Series
  - when `workerCategory` = *Optimized*: All, DV2-Series, EV3-Series

- **`worker`** (text)

- **`Instances`** (number)
  - depends on: `cluster`

- **`workerHours`** (number)
  - depends on: `cluster`

- **`workerHoursFactor`** (select)
  - depends on: `cluster`
  - options: Hours, Days, Month

- **`edgeCategory`** (select)
  - depends on: `cluster`
  - options: All, General Purpose, Optimized
  - when `cluster` = *HDInsight Machine Learning Services*: All, Compute Optimized, General Purpose, Optimized

- **`edgeInstanceSeries`** (select)
  - depends on: `cluster`, `edgeCategory`
  - options: All, A-Series, AV2-Series, DV2-Series, EV3-Series
  - when `cluster` = *HDInsight Machine Learning Services*: All, A-Series, AV2-Series, DV2-Series, EV3-Series, F-Series
  - when `edgeCategory` = *General Purpose*: All, A-Series, AV2-Series, DV2-Series
  - when `edgeCategory` = *Optimized*: All, DV2-Series, EV3-Series

- **`edge`** (text)

- **`edgeCount`** (number)

- **`edgeHours`** (number)
  - depends on: `edgeHoursFactor`
  - disappears when: `edgeHoursFactor` = *Days*

- **`edgeHoursFactor`** (select)
  - depends on: `edgeHoursFactor`
  - disappears when: `edgeHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`zookeeperCategory`** (select)
  - depends on: `cluster`
  - only exists when: `cluster` = *Interactive Query*, `cluster` = *HDInsight Machine Learning Services*, `cluster` = *Kafka*
  - options: All, General Purpose, Optimized

- **`zookeeperInstanceSeries`** (select)
  - depends on: `cluster`
  - only exists when: `cluster` = *Interactive Query*, `cluster` = *HDInsight Machine Learning Services*, `cluster` = *Kafka*
  - options: All, A-Series, AV2-Series, DV2-Series, EV3-Series

- **`zookeeperHours`** (number)
  - depends on: `cluster`
  - only exists when: `cluster` = *Interactive Query*, `cluster` = *HDInsight Machine Learning Services*

- **`zookeeperHoursFactor`** (select)
  - depends on: `cluster`
  - only exists when: `cluster` = *Interactive Query*, `cluster` = *HDInsight Machine Learning Services*
  - options: Hours, Days, Month

- **`mlServerHours`** (number)
  - depends on: `cluster`
  - only exists when: `cluster` = *HDInsight Machine Learning Services*

- **`mlServerHoursFactor`** (select)
  - depends on: `cluster`
  - only exists when: `cluster` = *HDInsight Machine Learning Services*
  - options: Hours, Days, Month

- **`Tier`** (select)
  - depends on: `cluster`
  - only exists when: `cluster` = *Kafka*
  - options: Standard, Premium

- **`Disk size`** (select)
  - depends on: `cluster`
  - only exists when: `cluster` = *Kafka*
  - options: S30 - 1024 GB

- **`Disks`** (number)
  - depends on: `cluster`
  - only exists when: `cluster` = *Kafka*

- **`Days`** (number)
  - depends on: `headHoursFactor`
  - only exists when: `headHoursFactor` = *Days*

- **`Days (headHoursFactor)`** (select)
  - depends on: `headHoursFactor`
  - only exists when: `headHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (workerHours)`** (number)
  - depends on: `workerHoursFactor`
  - only exists when: `workerHoursFactor` = *Days*

- **`Days (workerHoursFactor)`** (select)
  - depends on: `workerHoursFactor`
  - only exists when: `workerHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (edgeHours)`** (number)
  - depends on: `edgeHoursFactor`
  - only exists when: `edgeHoursFactor` = *Days*

- **`Days (edgeHoursFactor)`** (select)
  - depends on: `edgeHoursFactor`
  - only exists when: `edgeHoursFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Hdinsight",
  "name": "my-hdinsight",
  "fields": {
    "Region": "Central US",
    "Component": "Hadoop",
    "Category": "All",
    "Instance Series": "All",
    "Hours": 1
  }
}
```
