import React from 'react';
import {connect} from 'umi';
import styles from './WorkContent.less';

import Bookmark from '@/pages/Bookmark';
import Note from '@/pages/Note';
import Error404 from "./Error404";

const WorkContent: React.FC = (props: any) => {

  const {
    currentPage
  } = props;
  
  return (
    <div className={styles.container}>
      {
        (() => {
          switch (currentPage) {
            case 'note':
              return <Note/>;
            case 'bookmark':
              return <Bookmark/>;
            default:
              return <Error404/>;
          }
        })()
      }
    </div>
  )
}

export default connect(({global}) => ({
  currentPage: global.currentPage
}))(WorkContent);