<template>
  <div class="bastic-table">
    <div class="page-content">
      <el-table :data="tableData" style="width: 100%">
        <el-table-column prop="cik" label="CIK">
        </el-table-column>
        <el-table-column prop="ticker" label="TICKER">
        </el-table-column>
        <el-table-column prop="year" label="YEAR">
        </el-table-column>
        <el-table-column prop="state" label="STATE">
        </el-table-column>
        <el-table-column prop="office" label="OFFICE" width="240">
        </el-table-column>
        <el-table-column prop="eps" label="EPS">
        </el-table-column>
      </el-table>
      <div class="pagination">
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="currentPage"
          :page-sizes="[100, 200, 300, 400]"
          :page-size="100"
          layout="total, sizes, prev, pager, next, jumper"
          :total="400"
        >
        </el-pagination>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      currentPage: 1,
      tableData: [
        {
          cik: '1423579',
          ticker: 'LEGX',
          year: '2021',
          state: 'FL',
          office: 'Office of Trade & Services',
          eps: '3.16'
        },
        {
          cik: '715446',
          ticker: 'ANIX',
          year: '2021',
          state: 'CA',
          office: 'Office of Life Sciences',
          eps: '0'
        },
        {
          cik: '1687221',
          ticker: 'REVG',
          year: '2021',
          state: 'WI',
          office: 'Office of Manufacturing',
          eps: '2.03'
        },
        {
          cik: '825322',
          ticker: 'XDSL',
          year: '2021',
          state: 'MD',
          office: 'Office of Manufacturing',
          eps: '0'
        }
      ]
    }
  },
  methods: {
    handleSizeChange (val) {
      console.log(`${val}/page`)
    },
    handleCurrentChange (val) {
      console.log(`当前页: ${val}`)
    }
  }
}
</script>
