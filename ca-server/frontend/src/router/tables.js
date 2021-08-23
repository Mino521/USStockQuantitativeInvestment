import Basictable from '../views/tables/basic.vue'
import Fixedheadertable from '../views/tables/fixedheader.vue'

export default [{
  path: 'basic',
  name: 'basictable',
  component: Basictable,
  meta: ['Database1']
}, {
  path: 'fixedheader',
  name: 'fixedheadertable',
  component: Fixedheadertable,
  meta: ['Database2']
}]
